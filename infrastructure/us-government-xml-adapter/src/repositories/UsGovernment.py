import logging
import subprocess

logging.basicConfig()
log = logging.getLogger('[UsGovernment.py]')
log.setLevel(logging.DEBUG)

log.info('Starting...')


def votes():
    log.info('Invoking votes()')
    bash_command = '/congress/run'
    args = ['bash', '-c', bash_command]
    log.info(args)
    output = subprocess.check_output(args)
    return output
