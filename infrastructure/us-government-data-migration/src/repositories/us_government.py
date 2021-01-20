import logging
import subprocess
from os import path

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s [%(levelname)s] %(message)s",
)


congressRepoPath = path.join("..", "congress")

def run_task(task="", optional_args=[""]):
    command = [path.join(congressRepoPath, "run"), task] + optional_args
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    process.wait()


def votes():
    logging.info("Started downloading votes")
    run_task("votes")
    logging.info("Finished downloading votes")


def nominations():
    logging.info("Started downloading nominations")
    run_task("nominations", ["--congress=116"])
    logging.info("Finished downloading nominations")


def committee_meetings():
    logging.info("Started downloading committee Meetings")
    run_task("committee_meetings")
    logging.info("Finished downloading committee Meetings")


# Run once every 6hrs
def downloadBillXml():
    logging.info("Started downloading bills XML")
    run_task("govinfo", ["--bulkdata=BILLSTATUS", "--logs=info"])
    logging.info("Finished downloading bills XML")


def convertBillXmlToJson():
    logging.info("Started converting bills XML to JSON")
    run_task("bills", ["--logs=info"])
    logging.info("Finished converting bills XML to JSON")


def statutes():
    logging.info("Started downloading statutes")
    run_task("statutes")
    logging.info("Finished downloading statutes")


def legislative_members():
    logging.info("Started downloading list of legislative members")
    response = requests.get(
        "https://theunitedstates.io/congress-legislators/legislators-current.json"
    )

    if response.status_code != 200:
        response.raise_for_status()

    logging.info("Finished downloading list of legislative members")

    return response.json()


def bill_text():
    logging.info("Started downloading bills text")
    run_task(
        "govinfo",
        ["--collections=BILLS", "--bulkdata=False", "--store=text", "--logs=info"],
    )
    logging.info("Finished downloading bills text")
