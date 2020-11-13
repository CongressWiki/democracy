import logging
import json
from ..repositories import graphql_engine


logging.basicConfig()
log = logging.getLogger("[amendments.py]")
log.setLevel(logging.DEBUG)


def from_amendments_data(amendment_data):
    log.info("NEW AMENDMENT")

    amendment = {
        'id': amendment_data.get('amendment_id'),
        'actions': amendment_data.get('actions'),
        'amendment_type': amendment_data.get('amendment_type'),
        'amends_amendment': amendment_data.get('amends_amendment'),
        'amends_bill': amendment_data.get('amends_bill'),
        'amends_treaty': amendment_data.get('amends_treaty'),
        'chamber': amendment_data.get('chamber'),
        'congress': amendment_data.get('congress'),
        'description': amendment_data.get('description'),
        'introduced_at': amendment_data.get('introduced_at'),
        'number': amendment_data.get('number'),
        'purpose': amendment_data.get('purpose'),
        'sponsor': amendment_data.get('sponsor'),
        'status': amendment_data.get('status'),
        'status_at': amendment_data.get('status_at'),
        'updated_at': amendment_data.get('updated_at')
    }

    log.info(json.dumps(amendment))

    return graphql_engine.insert_amendment(amendment)
