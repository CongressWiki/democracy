import logging
import subprocess
from os import path

import requests


def run_task(task="", optional_args=['']):
    logging.info("Fetching " + task)

    command = [path.join("..", "congress", "run"), task] + optional_args

    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    process.wait()


def votes():
    run_task("votes")


def nominations():
    run_task("nominations", ["--congress=116"])


def committee_meetings():
    run_task("committee_meetings")


# Run once every 6hrs
def downloadBillXml():
    run_task("govinfo", ["--bulkdata=BILLSTATUS", "--logs=info"])


def convertBillXmlToJson():
    run_task("bills", ["--logs=info"])


def statutes():
    run_task("statutes")


def legislative_members():
    response = requests.get(
        "https://theunitedstates.io/congress-legislators/legislators-current.json"
    )

    if response.status_code != 200:
        response.raise_for_status()

    return response.json()


def bill_text():
    run_task(
        "govinfo",
        ["--collections=BILLS", "--bulkdata=False", "--store=text", "--logs=info"]
    )
