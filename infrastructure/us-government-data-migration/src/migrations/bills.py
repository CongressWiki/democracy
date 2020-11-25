import logging
import json
from ..repositories import graphql_engine


logging.basicConfig(
    filename="bills.log",
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)
log = logging.getLogger('')


def from_bills_data(bill_data):
    log.info("MIGRATING BILL")

    bill_keys = [
        "bill_id", "bill_type", "by_request", "congress", "number", "committee_reports", "introduced_at",
        "updated_at", "official_title", "popular_title",
        "short_title", "titles", "subjects_top_term",
        "subjects", "summary", "status", "status_at",
        "history", "enacted_as", "sponsor", "cosponsors",
        "committees", "amendments", "actions", "related_bills",
        "url"
    ]

    for key in bill_data:
        if key not in bill_keys:
            log.warn('Missed migration of Bill property: "' + key + '": ' + bill_data[key])

    bill = {
        'id': bill_data.get('bill_id'),
        'type': bill_data.get('bill_type'),
        'by_request': bill_data.get('by_request'),
        'congress': bill_data.get('congress'),
        'number': bill_data.get('number'),
        'committee_reports': bill_data.get('committee_reports'),
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
        'actions': bill_data.get('actions'),
        'related_bills': bill_data.get('related_bills'),
        'url': bill_data.get('url')
    }

    try:
        graphql_engine.insert_bill(bill)
    except Exception as error:
        log.warn(type(error))
        log.warn(error)
        log.warn(json.dumps(bill))
