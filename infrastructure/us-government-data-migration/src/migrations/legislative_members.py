import logging
import json
from ..repositories import graphql_engine

logging.basicConfig()
log = logging.getLogger('[legislative_members.py]')
log.setLevel(logging.DEBUG)


def from_legislative_member(legislative_member):
    member_id = legislative_member.get('id')
    member_name = legislative_member.get('name')
    member_bio = legislative_member.get('bio')
    member_terms = legislative_member.get('terms')
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

    log.info('NEW MEMBER')
    log.info(json.dumps(new_member))

    return graphql_engine.insert_legislative_member(new_member)
