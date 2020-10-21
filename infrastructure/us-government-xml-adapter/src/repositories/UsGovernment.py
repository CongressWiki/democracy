import logging
import subprocess
from os import path

logging.basicConfig()
log = logging.getLogger('[UsGovernment.py]')
log.setLevel(logging.DEBUG)


def run_task(task=''):
    log.info("Fetching " + task)

    command = [path.join('congress', 'run'), task]
    log.info(command)

    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    process.wait()


def votes():
    run_task('votes')
