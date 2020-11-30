import json
import logging

from ..repositories import graphql_engine


def from_bills_data(bill_data: dict):
    logging.debug("MIGRATING BILL")

    check_for_missing_props(bill_data)

    migrate_bill(bill_data)
    migrate_bill_actions(bill_data)
    migrate_bill_subjects(bill_data)


def check_for_missing_props(bill_data: dict):
    bill_keys = [
        "bill_id",
        "bill_type",
        "by_request",
        "congress",
        "number",
        "committee_reports",
        "introduced_at",
        "updated_at",
        "official_title",
        "popular_title",
        "short_title",
        "titles",
        "subjects_top_term",
        "subjects",
        "summary",
        "status",
        "status_at",
        "history",
        "enacted_as",
        "sponsor",
        "cosponsors",
        "committees",
        "amendments",
        "actions",
        "related_bills",
        "url",
    ]

    for key in bill_data:
        if key not in bill_keys:
            logging.warn(
                'Missed migration of Bill property: "'
                + key
                + '": '
                + json.dumps(bill_data[key])
            )


def migrate_bill(bill_data: dict):
    bill_requested_by = bool(bill_data.get("by_request"))
    bill_summary_text = get_summary_text(bill_data)
    bill_sponsor_id = get_sponsor_id(bill_data)

    bill = {
        "id": bill_data.get("bill_id"),
        "type": bill_data.get("bill_type"),
        "by_request": bill_requested_by,
        "number": bill_data.get("number"),
        "subject": bill_data.get("subjects_top_term"),
        "introduced_at": bill_data.get("introduced_at"),
        "updated_at": bill_data.get("updated_at"),
        "title": bill_data.get("official_title"),
        "summary": bill_summary_text if bill_summary_text else '',
        "status": bill_data.get("status"),
        "congress_id": bill_data.get("congress"),
        "sponsor_id": bill_sponsor_id if bill_sponsor_id else ''
        # "committee_reports": bill_data.get("committee_reports"),
        # "congress": bill_data.get("congress"),
        # "popular_title": bill_data.get("popular_title"),
        # "short_title": bill_data.get("short_title"),
        # "titles": bill_data.get("titles"),
        # "subjects": bill_data.get("subjects"),
        # "status_at": bill_data.get("status_at"),
        # "history": bill_data.get("history"),
        # "enacted_as": bill_data.get("enacted_as"),
        # "sponsor": bill_data.get("sponsor"),
        # "cosponsors": bill_data.get("cosponsors"),
        # "committees": bill_data.get("committees"),
        # "amendments": bill_data.get("amendments"),
        # "actions": bill_data.get("actions"),
        # "related_bills": bill_data.get("related_bills"),
        # "url": bill_data.get("url"),
    }

    try:
        graphql_engine.insert_bill(bill)
    except Exception as error:
        logging.warn('Error inserting bill.')
        logging.warn(error)


def migrate_bill_actions(bill_data: dict):
    bill_actions = bill_data.get("actions")

    for index, bill_action in enumerate(bill_actions):
        action_code = bill_action.get('code')
        action = {
            "id": bill_data.get('bill_id') + '-' + f"{index}",
            "bill_id": bill_data.get('bill_id'),
            "type": bill_action.get('type'),
            "code": action_code if action_code else '',
            "text": bill_action.get('text'),
            "acted_at": bill_action.get('acted_at')
        }

        try:
            graphql_engine.insert_action(action)
        except Exception as error:
            logging.warn('Error inserting bill.')
            logging.warn(error)


def migrate_committees(bill_data: dict):
    bill_committees = bill_data.get("committees")

    for bill_committee in bill_committees:
        committee = {
            "id": bill_committee.get('committee_id'),
            "name": bill_committee.get('committee')
        }

        try:
            graphql_engine.insert_committee(committee)
        except Exception as error:
            logging.warn(type(error))
            logging.warn(error)
            logging.warn(json.dumps(committee))

        committee_has_bill = {
            "bill_id": bill_data.get('bill_id'),
            "committee_id": committee.get('id')
        }

        try:
            graphql_engine.insert_committee_has_bill(committee_has_bill)
        except Exception as error:
            logging.warn('Error inserting bill.')
            logging.warn(error)


def migrate_bill_subjects(bill_data: dict):
    bill_subjects = bill_data.get('subjects')

    for bill_subject in bill_subjects:
        subject = {
            "value": bill_subject,
            "comment": ""
        }

        try:
            graphql_engine.insert_bill_subjects(subject)
        except Exception as error:
            logging.warn('Error inserting bill.')
            logging.warn(error)


def get_summary_text(bill_data: dict):
    bill_summary_payload = bill_data.get("summary")

    if isinstance(bill_summary_payload, dict):
        return bill_summary_payload.get("text")

    return None


def get_sponsor_id(bill_data: dict):
    sponsor = bill_data.get("sponsor")

    if isinstance(sponsor, dict):
        return sponsor.get('bioguide_id')

    return None
