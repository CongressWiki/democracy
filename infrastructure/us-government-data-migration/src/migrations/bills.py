import json
import logging
from datetime import date, datetime

from ..repositories import graphql_engine


def from_bills_data(bill_data: dict):
    logging.info(f"MIGRATING BILL {bill_data.get('bill_id')}")

    check_for_missing_props(bill_data)

    migrate_bill(bill_data)
    # migrate_bill_actions(bill_data)
    # migrate_bill_subjects(bill_data)
    # migrate_bill_sponsors(bill_data)
    migrate_committees(bill_data)


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
    summary_text = get_summary_text(bill_data)
    sponsor_id = get_sponsor_id(bill_data)

    introduced_at = bill_data.get("introduced_at")
    introduced_at_date = datetime.fromisoformat(introduced_at)

    status_at = bill_data.get("status_at")
    status_at_date = datetime.fromisoformat(status_at)

    updated_at = bill_data.get("updated_at")
    updated_at_date = datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%SZ")

    subject = get_subject(bill_data)

    bill = {
        "id": bill_data.get("bill_id"),
        "type": bill_data.get("bill_type"),
        "by_request": bool(bill_data.get("by_request")),
        "number": int(bill_data.get("number")),
        "subject": subject,
        "introduced_at": introduced_at_date.strftime("%Y-%m-%dT%H:%M:%S.%f+00:00"),
        "updated_at": updated_at_date.strftime("%Y-%m-%dT%H:%M:%S.%f+00:00"),
        "title": bill_data.get("official_title"),
        "summary": summary_text or 'No summary available.',
        "status": bill_data.get("status"),
        "status_at": status_at_date.strftime("%Y-%m-%dT%H:%M:%S.%f+00:00"),
        "congress": bill_data.get("congress"),
        "actions": bill_data.get("actions"),
        "sponsor": sponsor_id,
        # "committee_reports": bill_data.get("committee_reports"),
        # "popular_title": bill_data.get("popular_title"),
        # "short_title": bill_data.get("short_title"),
        # "titles": bill_data.get("titles"),
        # "subjects": bill_data.get("subjects"),
        # "status_at": bill_data.get("status_at"),
        # "history": bill_data.get("history"),
        # "enacted_as": bill_data.get("enacted_as"),
        # "cosponsors": bill_data.get("cosponsors"),
        # "committees": bill_data.get("committees"),
        # "amendments": bill_data.get("amendments"),
        # "related_bills": bill_data.get("related_bills"),
        # "url": bill_data.get("url"),
    }

    try:
        graphql_engine.insert_bill(bill)
    except Exception as error:
        logging.warn(type(error))
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
            graphql_engine.insert_bill_action(action)
        except Exception as error:
            logging.warn(type(error))
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
            logging.warn(type(error))
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


def get_subject(bill_data: dict):
    subjects_top_term = bill_data.get("subjects_top_term")
    other_subjects = bill_data.get("subjects")

    if subjects_top_term:
        return subjects_top_term

    if isinstance(other_subjects, list) and len(other_subjects) > 0:
        return other_subjects[0]

    return 'none'
