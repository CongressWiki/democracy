import logging
from repositories import us_government
from migrations import legislative_members, proposals, votes, bills
import utils
import os

logging.basicConfig()
log = logging.getLogger('[run.py]')
log.setLevel(logging.DEBUG)


def collect_data_file_paths():
    rootdir = os.path.join('data')
    votes = []

    for root, dirs, files in os.walk(rootdir):
        for name in files:
            if name.endswith((".json")):
                full_path = os.path.join(root, name)
                votes.append(full_path)
    return votes


def migrate_legislative_members():
    members = us_government.legislative_members()

    for member in members:
        legislative_members.from_legislative_member(member)


def migrate_bills():
    bills_data = us_government.govinfo()

    for bill in bills:
        bills.from_bills_data(bills_data)


def migrate_votes():
    us_government.votes()
    vote_file_paths = collect_data_file_paths()

    for vote_file_path in vote_file_paths:
        vote_data = utils.read_json_file(vote_file_path)
        proposals.from_vote_data(vote_data)
        votes.from_vote_data(vote_data)


migrate_legislative_members()
migrate_bills()
migrate_votes()
