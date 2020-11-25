import logging
import json
from ..repositories import graphql_engine

logging.basicConfig(
    filename="legislative_members.log",
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)
log = logging.getLogger('')


def from_legislative_member(legislative_member_data):
    log.info("MIGRATING LEGISLATIVE MEMBER")

    legislative_member_keys = [
        "id", "name", "bio", "terms"
    ]

    for key in legislative_member_data:
        if key not in legislative_member_keys:
            log.warn(
                'Missed migration of Legislative Member property: "' +
                key + '": ' +
                json.dumps(legislative_member_data[key])
            )

    member_id = legislative_member_data.get('id')
    member_name = legislative_member_data.get('name')
    member_bio = legislative_member_data.get('bio')
    member_terms = legislative_member_data.get('terms')
    last_active_term = member_terms[-1]

    new_member = {
        'id': member_id.get('lis') or member_id.get('bioguide') or member_id.get('govtrack'),
        'bioguide': member_id.get('bioguide'),
        'govtrack': member_id.get('govtrack'),
        'lis': member_id.get('lis'),
        'first_name': member_name.get('first'),
        'last_name': member_name.get('last'),
        'official_full': member_name.get('official_full'),
        'gender': member_bio.get('gender'),
        'birthday': member_bio.get('birthday'),
        'isSenateMember': bool(last_active_term.get('type') == 'sen'),
        'isHouseMember': bool(last_active_term.get('type') == 'rep'),
        'party': last_active_term.get('party'),
        'state': last_active_term.get('state'),
        'state_rank': last_active_term.get('state_rank'),
        'bio_url': last_active_term.get('url'),
        'address': last_active_term.get('address'),
        'phone': last_active_term.get('phone'),
        'contact_form_url': last_active_term.get('contact_form'),
        'terms': member_terms,
    }

    try:
        return graphql_engine.insert_legislative_member(new_member)
    except Exception as error:
        log.warn(type(error))
        log.warn(error)
        log.warn(json.dumps(new_member))
