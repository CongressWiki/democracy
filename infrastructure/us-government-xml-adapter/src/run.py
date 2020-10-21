import logging
from repositories import UsGovernment

logging.basicConfig()
log = logging.getLogger('[run.py]')
log.setLevel(logging.DEBUG)

log.info('Starting...')

output = UsGovernment.votes()

log.info(output)
