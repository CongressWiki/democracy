import logging
from repositories import UsGovernment

logging.basicConfig()
log = logging.getLogger('[run.py]')
log.setLevel(logging.DEBUG)

log.info('Starting')

UsGovernment.votes()
