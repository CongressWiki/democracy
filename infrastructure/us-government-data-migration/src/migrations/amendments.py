import json
import logging

from ..repositories import graphql_engine


def from_amendments_data(amendment_data: dict):
    logging.info(f"MIGRATING AMENDMENT {amendment_data.get('amendment_id')}")

    check_for_missing_props(amendment_data)

    migrate_amendment(amendment_data)
    migrate_amendment_actions(amendment_data)
    migrate_amendment_sponsors(amendment_data)


def migrate_amendment(amendment_data: dict):
    amendment_purpose = amendment_data.get("purpose")
    amendment_description = amendment_data.get("description")
    amendment_amends_bill = amendment_data.get("amends_bill")
    amendment_amends_treaty = amendment_data.get("amends_treaty")
    amendment_amends_amendment = amendment_data.get("amends_amendment")

    amendment = {
        "id": amendment_data.get("amendment_id"),
        "type": amendment_data.get("amendment_type"),
        "bill_id": amendment_amends_bill.get("bill_id") if amendment_amends_bill else None,
        "treaty_id": amendment_amends_treaty.get('id') if amendment_amends_treaty else None,
        "amendment_id": amendment_amends_amendment.get('amendment_id') if amendment_amends_amendment else None,
        "chamber": amendment_data.get("chamber"),
        "number": int(amendment_data.get("number")),
        "congress_id": amendment_data.get("congress"),
        "description": amendment_description if amendment_description else '',
        "purpose": amendment_purpose if amendment_purpose else '',
        "status": amendment_data.get("status"),
        "introduced_at": amendment_data.get("introduced_at"),
        "updated_at": amendment_data.get("updated_at"),
        "proposed_at": amendment_data.get("proposed_at")
    }

    try:
        return graphql_engine.insert_amendment(amendment)
    except Exception as error:
        logging.warn('Error inserting amendment.')
        logging.warn(error)


def migrate_amendment_actions(amendment_data: dict):
    amendment_actions = amendment_data.get("actions")

    for index, amendment_action in enumerate(amendment_actions):
        action_code = amendment_action.get('code')
        action = {
            "id": amendment_data.get('amendment_id') + '-' + f"{index}",
            "amendment_id": amendment_data.get('amendment_id'),
            "type": amendment_action.get('type'),
            "code": action_code if action_code else '',
            "text": amendment_action.get('text'),
            "acted_at": amendment_action.get('acted_at')
        }

        try:
            graphql_engine.insert_amendment_action(action)
        except Exception as error:
            logging.warn('Error inserting amendment.')
            logging.warn(error)


def migrate_amendment_sponsors(amendment_data: dict):
    amendment_cosponsors = amendment_data.get("cosponsors")

    if not isinstance(amendment_cosponsors, list):
        return

    for index, amendment_cosponsor in enumerate(amendment_cosponsors):
        cosponsorship = {
            "id": amendment_data.get('amendment_id') + '-' + amendment_cosponsor.get('bioguide_id'),
            "legislative_member_id": amendment_cosponsor.get('bioguide_id'),
            "amendment_id": amendment_data.get('amendment_id'),
            "original_cosponsor": bool(amendment_cosponsor.get('original_cosponsor')),
            "sponsored_at": amendment_cosponsor.get('sponsored_at'),
            "withdrawn_at": amendment_cosponsor.get('withdrawn_at')
        }

        try:
            graphql_engine.insert_amendment_cosponsorship(cosponsorship)
        except Exception as error:
            logging.warn('Error inserting amendment.')
            logging.warn(error)


def check_for_missing_props(amendment_data: dict):
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
