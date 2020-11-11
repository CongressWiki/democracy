import logging
import json
from ..repositories import graphql_engine


logging.basicConfig()
log = logging.getLogger("[bills.py]")
log.setLevel(logging.DEBUG)


def from_bills_data(bill_data):
    log.info("NEW BILL")

    bill = {
        'id': bill_data.get('bill_id'),
        'introduced_at': bill_data.get('introduced_at'),
        'updated_at': bill_data.get('updated_at'),
        'official_title': bill_data.get('official_title'),
        'popular_title': bill_data.get('popular_title'),
        'short_title': bill_data.get('short_title'),
        'titles': bill_data.get('titles'),
        'subjects_top_term': bill_data.get('subjects_top_term'),
        'subjects': bill_data.get('subjects'),
        'summary': bill_data.get('summary'),
        'status': bill_data.get('status'),
        'status_at': bill_data.get('status_at'),
        'history': bill_data.get('history'),
        'enacted_as': bill_data.get('enacted_as'),
        'sponsor': bill_data.get('sponsor'),
        'cosponsors': bill_data.get('cosponsors'),
        'committees': bill_data.get('committees'),
        'amendments': bill_data.get('amendments'),
        'actions': bill_data.get('actions')
    }

    log.info(json.dumps(bill))

    return graphql_engine.insert_bill(bill)
