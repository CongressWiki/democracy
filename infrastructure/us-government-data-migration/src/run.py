import logging
from .repositories import us_government
from .migrations import legislative_members, proposals, votes, bills, amendments
from . import utils
import os

logging.basicConfig()
log = logging.getLogger('[run.py]')
log.setLevel(logging.DEBUG)


def downloadVotes():
    us_government.votes()


def downloadBillsAndAmendments():
    us_government.govinfo()
    us_government.bills()


def collect_data_file_paths():
    rootdir = os.path.join('data')
    bill_file_paths = []
    amendment_file_paths = []
    vote_file_paths = []

    log.info('Gathering file paths for downloaded US government files.')

    for root, _dirs, files in os.walk(rootdir):
        if 'bills' in root:
            for name in files:
                if name.endswith((".json")):
                    full_path = os.path.join(root, name)
                    bill_file_paths.append(full_path)
        if 'amendments' in root:
            for name in files:
                if name.endswith((".json")):
                    full_path = os.path.join(root, name)
                    amendment_file_paths.append(full_path)
        if 'votes' in root:
            for name in files:
                if name.endswith((".json")):
                    full_path = os.path.join(root, name)
                    vote_file_paths.append(full_path)

    return bill_file_paths, amendment_file_paths, vote_file_paths


def migrate_legislative_members():
    members = us_government.legislative_members()

    for member in members:
        legislative_members.from_legislative_member(member)


def migrate_bills(bill_file_paths):
    for bill_file_path in bill_file_paths:
        bill_data = utils.read_json_file(bill_file_path)
        bills.from_bills_data(bill_data)

    log.info('Finished migration of bills')


def migrate_amendments(amendment_file_paths):
    for amendment_file_path in amendment_file_paths:
        amendment_data = utils.read_json_file(amendment_file_path)
        amendments.from_amendments_data(amendment_data)

    log.info('Finished migration of amendments')


def migrate_votes(vote_file_paths):
    for vote_file_path in vote_file_paths:
        vote_data = utils.read_json_file(vote_file_path)
        proposals.from_vote_data(vote_data)
        votes.from_vote_data(vote_data)

    log.info('Finished migration of votes')


# Download and parse the data from official resources
downloadVotes()
downloadBillsAndAmendments()

# Gather the file paths of the downloaded files
bill_file_paths, amendment_file_paths, vote_file_paths = collect_data_file_paths()

# Insert data into database
migrate_bills(bill_file_paths)
migrate_amendments(amendment_file_paths)
migrate_votes(vote_file_paths)
migrate_legislative_members()
