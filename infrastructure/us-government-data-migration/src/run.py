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
    bills = []

    for root, dirs, files in os.walk(rootdir):
        if 'bills' in root:
            for name in files:
                if name.endswith((".json")):
                    full_path = os.path.join(root, name)
                    bills.append(full_path)
    return bills


def migrate_legislative_members():
    members = us_government.legislative_members()

    for member in members:
        legislative_members.from_legislative_member(member)


def migrate_bills():
    # us_government.govinfo()
    # us_government.bills()
    log.info('Started migration of bills')
    bill_file_paths = collect_data_file_paths()
    log.info('Collected all file paths')

    for bill_file_path in bill_file_paths:
        bill_data = utils.read_json_file(bill_file_path)
        bills.from_bills_data(bill_data)

    log.info('Finished migration of bills')


def migrate_votes():
    # us_government.votes()
    log.info('Started migration of votes')
    vote_file_paths = collect_data_file_paths()

    for vote_file_path in vote_file_paths:
        vote_data = utils.read_json_file(vote_file_path)
        proposals.from_vote_data(vote_data)
        votes.from_vote_data(vote_data)


migrate_bills()
# migrate_legislative_members()
# migrate_votes()
