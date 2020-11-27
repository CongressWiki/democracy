import logging
import subprocess
import requests
from os import path

logging.basicConfig()
log = logging.getLogger("[UsGovernment.py]")
log.setLevel(logging.DEBUG)


def run_task(task="", args=[]):
    log.info("Fetching " + task)

    command = [path.join("..", "congress", "run"), task] + args + ["--log=info"]
    log.info(command)

    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    process.wait()


def votes():
    run_task("votes")


def nominations():
    run_task("nominations")


def committee_meetings():
    run_task("committee_meetings")


# Run once every 6hrs
def downloadBillXml():
    run_task("govinfo", ["--bulkdata=BILLSTATUS"])


def convertBillXmlToJson():
    run_task("bills")


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
        ["--collections=BILLS", "--store=pdf,mods,xml,text", "--bulkdata=False"],
    )
