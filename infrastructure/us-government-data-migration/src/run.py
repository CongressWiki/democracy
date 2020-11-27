import logging
from .repositories import us_government
from .migrations import (
    legislative_members,
    proposals,
    votes,
    bills,
    amendments,
    nominations,
)
from . import utils
import os

logging.basicConfig(
    filename="run.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
log = logging.getLogger(__name__)


#############
# Downloads #
#############


def download_votes():
    us_government.votes()


def download_bills_and_amendments():
    us_government.downloadBillXml()
    us_government.convertBillXmlToJson()
    us_government.bill_text()


def download_nominations():
    us_government.nominations()


#####################
# Collect downloads #
#####################


def collect_data_file_paths():
    rootdir = os.path.join("data")
    bill_file_paths = []
    amendment_file_paths = []
    vote_file_paths = []
    nomination_file_paths = []

    log.info("Gathering file paths for downloaded US government files.")

    for root, _dirs, files in os.walk(rootdir):
        json_extension = ".json"
        if "bills" in root:
            for name in files:
                if name.endswith((json_extension)):
                    full_path = os.path.join(root, name)
                    bill_file_paths.append(full_path)
        if "amendments" in root:
            for name in files:
                if name.endswith((json_extension)):
                    full_path = os.path.join(root, name)
                    amendment_file_paths.append(full_path)
        if "votes" in root:
            for name in files:
                if name.endswith((json_extension)):
                    full_path = os.path.join(root, name)
                    vote_file_paths.append(full_path)
        if "nominations" in root:
            for name in files:
                if name.endswith((json_extension)):
                    full_path = os.path.join(root, name)
                    vote_file_paths.append(full_path)

    return bill_file_paths, amendment_file_paths, vote_file_paths, nomination_file_paths


##############
# Migrations #
##############


def migrate_legislative_members():
    members = us_government.legislative_members()

    for member in members:
        legislative_members.from_legislative_member(member)


def migrate_bills(bill_file_paths):
    for bill_file_path in bill_file_paths:
        bill_data = utils.read_json_file(bill_file_path)
        bills.from_bills_data(bill_data)

    log.info("Finished migration of bills")


def migrate_amendments(amendment_file_paths):
    for amendment_file_path in amendment_file_paths:
        amendment_data = utils.read_json_file(amendment_file_path)
        amendments.from_amendments_data(amendment_data)

    log.info("Finished migration of amendments")


def migrate_votes(vote_file_paths):
    for vote_file_path in vote_file_paths:
        vote_data = utils.read_json_file(vote_file_path)
        proposals.from_vote_data(vote_data)
        votes.from_vote_data(vote_data)

    log.info("Finished migration of votes")


def migrate_nominations(nomination_file_paths):
    for nomination_file_path in nomination_file_paths:
        nomination_data = utils.read_json_file(nomination_file_path)
        nominations.from_nomination_data(nomination_data)

    log.info("Finished migration of votes")


###############
# Invocations #
###############


# Download and parse the data from official resources
download_votes()
download_bills_and_amendments()
download_nominations()

# Gather the file paths of the downloaded files
(
    bill_file_paths,
    amendment_file_paths,
    vote_file_paths,
    nomination_file_paths,
) = collect_data_file_paths()

# Insert data into database
migrate_bills(bill_file_paths)
migrate_amendments(amendment_file_paths)
migrate_votes(vote_file_paths)
migrate_legislative_members()
# migrate_nominations(nomination_file_paths)
