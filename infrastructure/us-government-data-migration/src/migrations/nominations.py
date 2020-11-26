import logging
import json
from ..repositories import graphql_engine


logging.basicConfig(
    filename="temp/nominations.log",
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)
log = logging.getLogger('')


def from_nominations_data(nomination_data):
    log.info("MIGRATING NOMINATION")

    nomination_keys = [
        "id"
    ]

    for key in nomination_data:
        if key not in nomination_keys:
            log.warn('Missed migration of Bill property: "' + key + '": ' + nomination_data[key])

    nomination = {
        'id': nomination_data.get('nomination_id')
    }

    try:
        return graphql_engine.insert_nomination(nomination)
    except Exception as error:
        log.warn(type(error))
        log.warn(error)
        log.warn(json.dumps(nomination))
