import json
import logging

from ..repositories import graphql_engine


def from_amendments_data(amendment_data):
    logging.debug("MIGRATING AMENDMENT")

    amendment_keys = [
        "actions",
        "amendment_id",
        "amendment_type",
        "amends_amendment",
        "amends_bill",
        "amends_treaty",
        "chamber",
        "congress",
        "description",
        "introduced_at",
        "number",
        "purpose",
        "sponsor",
        "status",
        "status_at",
        "updated_at",
        "proposed_at"
    ]

    for key in amendment_data:
        if key not in amendment_keys:
            logging.warn(
                'Missed migration of Amendment property: "'
                + key
                + '": '
                + json.dumps(amendment_data[key])
            )

    amendment = {
        "id": amendment_data.get("amendment_id"),
        "actions": amendment_data.get("actions"),
        "type": amendment_data.get("amendment_type"),
        "amends_amendment": amendment_data.get("amends_amendment"),
        "amends_bill": amendment_data.get("amends_bill"),
        "amends_treaty": amendment_data.get("amends_treaty"),
        "chamber": amendment_data.get("chamber"),
        "congress": amendment_data.get("congress"),
        "description": amendment_data.get("description"),
        "introduced_at": amendment_data.get("introduced_at"),
        "number": amendment_data.get("number"),
        "purpose": amendment_data.get("purpose"),
        "sponsor": amendment_data.get("sponsor"),
        "status": amendment_data.get("status"),
        "status_at": amendment_data.get("status_at"),
        "updated_at": amendment_data.get("updated_at"),
        "proposed_at": amendment_data.get("proposed_at")
    }

    try:
        return graphql_engine.insert_amendment(amendment)
    except Exception as error:
        logging.warn(type(error))
        logging.warn(error)
        logging.warn(json.dumps(amendment))
