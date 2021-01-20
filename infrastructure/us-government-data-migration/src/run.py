import logging
import os

from dotenv import load_dotenv

from . import utils
from .migrations import (amendments, bills, legislative_members, nominations,
                         votes)
from .repositories import us_government

if os.environ.get("EC2_HOSTNAME") is None:
    load_dotenv()


logging.basicConfig(
    # handlers=[logging.FileHandler("migrations.log"), logging.StreamHandler()],
    level=logging.INFO,
    format="%(asctime)s - %(name)s [%(levelname)s] %(message)s",
)


#############
# Downloads #
#############
def download_votes():
    us_government.votes()


def download_bills_and_amendments():
    us_government.downloadBillXml()
    us_government.convertBillXmlToJson()


def download_bills_text():
    us_government.bill_text()


def download_nominations():
    us_government.nominations()


####################################
# Gather paths of downloaded files #
####################################
buildDirPath = os.path.join("..", "..", "build")


def collect_data_file_paths():
    rootdir = os.path.join(buildDirPath, "us-government-data")
    bill_file_paths = []
    amendment_file_paths = []
    vote_file_paths = []
    nomination_file_paths = []

    logging.info("Started gathering file paths for downloaded US government files")

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

    logging.info("Finished gathering file paths for downloaded US government files")

    return (
        bill_file_paths,
        amendment_file_paths,
        vote_file_paths,
        nomination_file_paths,
    )


##############
# Migrations #
##############
def download_and_migrate_legislative_members():
    logging.info("Started download & migration of legislative members")
    for member in us_government.legislative_members():
        legislative_members.from_legislative_member(member)
    logging.info("Finished download & migration of legislative members")


def migrate_bills(bill_file_paths):
    logging.info("Started migration of bills")
    for bill_file_path in bill_file_paths:
        bill_data = utils.read_json_file(bill_file_path)
        bills.from_bills_data(bill_data)

    logging.info("Finished migration of bills")


def migrate_amendments(amendment_file_paths):
    logging.info("Started migration of amendments")
    for amendment_file_path in amendment_file_paths:
        amendment_data = utils.read_json_file(amendment_file_path)
        amendments.from_amendments_data(amendment_data)

    logging.info("Finished migration of amendments")


def migrate_votes(vote_file_paths):
    logging.info("Started migration of votes")
    for vote_file_path in vote_file_paths:
        vote_data = utils.read_json_file(vote_file_path)
        votes.from_vote_data(vote_data)

    logging.info("Finished migration of votes")


def migrate_nominations(nomination_file_paths):
    logging.info("Started migration of votes")
    for nomination_file_path in nomination_file_paths:
        nomination_data = utils.read_json_file(nomination_file_path)
        nominations.from_nomination_data(nomination_data)

    logging.info("Finished migration of votes")


###############
# Invocations #
###############

# Download and parse the data from official resources #

# download_nominations() # Broken: Points at deprecated website
download_votes()
download_bills_and_amendments()
# download_bills_text()
download_and_migrate_legislative_members()


# Gather the file paths of the downloaded files #

(
    bill_file_paths,
    amendment_file_paths,
    vote_file_paths,
    nomination_file_paths,
) = collect_data_file_paths()


# Insert data into database #

migrate_votes(vote_file_paths)
migrate_bills(bill_file_paths)
# migrate_nominations(nomination_file_paths)
# migrate_amendments(amendment_file_paths)
