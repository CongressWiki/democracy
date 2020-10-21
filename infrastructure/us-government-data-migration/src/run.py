import logging
from repositories import us_government
import migrations
import utils
import os

logging.basicConfig()
log = logging.getLogger('[run.py]')
log.setLevel(logging.DEBUG)


def fetch_all_us_government_data():
    us_government.votes()
    us_government.govinfo()
    us_government.bills()
    us_government.nominations()
    us_government.committee_meetings()
    us_government.statutes()


def collect_data_file_paths():
    rootdir = os.path.join('data')
    votes = []

    for root, dirs, files in os.walk(rootdir):
        for name in files:
            if name.endswith((".json")):
                full_path = os.path.join(root, name)
                votes.append(full_path)
    return votes


def migrate_legislative_data():
    legislative_members = us_government.legislative_members()
    migrations.senate_members.from_legislative_members(legislative_members)
    migrations.house_members.from_legislative_members(legislative_members)


def migrate_vote_data():
    # us_government.votes()
    vote_file_paths = collect_data_file_paths()

    for vote_file_path in vote_file_paths:
        vote_data = utils.read_json_file(vote_file_path)
        migrations.proposals.from_vote_data(vote_data)


migrate_vote_data()
