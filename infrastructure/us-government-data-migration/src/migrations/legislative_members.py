import json
import logging
from datetime import date, datetime

from ..repositories import graphql_engine

SENATOR = "senator"
HOUSE_REPRESENTATIVE = "house_representative"


def from_legislative_member(legislative_member_data):
    check_for_missing_properties(legislative_member_data)
    migrate_member(legislative_member_data)
    migrate_elected_official(legislative_member_data)


def check_for_missing_properties(legislative_member_data):
    logging.debug("MIGRATING LEGISLATIVE MEMBER")

    legislative_member_keys = [
        "id", "name", "bio", "terms",
        "leadership_roles", "family", "other_names"
    ]

    for key in legislative_member_data:
        if key not in legislative_member_keys:
            logging.warn(
                'Missed migration of Legislative Member property: "'
                + key
                + '": '
                + json.dumps(legislative_member_data[key])
            )


def migrate_member(legislative_member_data):
    member_ids = legislative_member_data.get("id")
    member_name = legislative_member_data.get("name")
    member_bio = legislative_member_data.get("bio")
    member_terms = legislative_member_data.get("terms")
    last_active_term = member_terms[-1]

    birthday = member_bio.get("birthday")
    born_date = datetime.fromisoformat(birthday)
    born_at = born_date.strftime("%Y-%m-%dT%H:%M:%S.%f+00:00")

    updated_at = datetime.now()

    preferred_name = member_name.get("official_full") or (member_name.get("first") + ' ' + member_name.get("last"))

    new_member = {
        "id": member_ids.get("bioguide"),
        "preferred_name": preferred_name,
        "first_name": member_name.get("first"),
        "last_name": member_name.get("last"),
        "gender": member_bio.get("gender"),
        "state": last_active_term.get("state"),
        "image_url": "",
        "is_government_official": True,
        "political_party_id": last_active_term.get("party"),
        "born_at": born_at,
        "updated_at": updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f+00:00")
    }

    try:
        return graphql_engine.insert_member(new_member)
    except Exception as error:
        logging.warn(type(error))
        logging.warn(error)


def migrate_elected_official(legislative_member_data):
    member_ids = legislative_member_data.get("id")

    member_terms = legislative_member_data.get("terms")
    last_active_term = member_terms[-1]

    position = get_position(last_active_term)

    start_of_term = last_active_term.get('start')
    end_of_term = last_active_term.get('end')

    service_start_date = datetime.fromisoformat(start_of_term)
    service_end_date = datetime.fromisoformat(end_of_term)

    service_start_at = service_start_date.strftime("%Y-%m-%dT%H:%M:%S.%f+00:00")
    service_end_at = service_end_date.strftime("%Y-%m-%dT%H:%M:%S.%f+00:00")

    updated_at = datetime.now()

    house_term_count = get_count_of_position_terms(member_terms, HOUSE_REPRESENTATIVE)
    senate_term_count = get_count_of_position_terms(member_terms, SENATOR)

    is_active = is_term_active(service_end_date)

    new_elected_official = {
        "id": member_ids.get("bioguide") + "-" + position + "-" + service_start_date.strftime("%Y"),
        "position": position,
        "is_active": is_active,
        "member_id": member_ids.get("bioguide"),
        "political_party_id": last_active_term.get("party"),
        "position": position,
        "rank": last_active_term.get("state_rank"),
        "state": last_active_term.get("state"),
        "district": last_active_term.get('district'),
        "house_terms": house_term_count,
        "senate_terms": senate_term_count,
        "description": "",
        "service_start_at": service_start_at,
        "service_end_at": service_end_at,
        "updated_at": updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f+00:00")
    }

    try:
        return graphql_engine.insert_elected_official(new_elected_official)
    except Exception as error:
        logging.warn(type(error))
        logging.warn(error)


# def migrate_political_parties(legislative_member_data):

#     new_political_party = {
#         "id": "dem",
#         "name":
#     }

#     try:
#         return graphql_engine.insert_elected_official(new_elected_official)
#     except Exception as error:
#         logging.warn(type(error))
#         logging.warn(error)
#         logging.warn(json.dumps(new_elected_official))


def get_position(last_active_term):
    term_type = last_active_term.get('type')

    if term_type == 'sen':
        return SENATOR
    if term_type == 'rep':
        return HOUSE_REPRESENTATIVE


def is_term_active(service_end_date):
    present = datetime.now()
    return bool(service_end_date < present)


def get_count_of_position_terms(terms, position):
    count = 0
    for term in terms:
        position = get_position(term)
        if position == position:
            count = count + 1

    return count
