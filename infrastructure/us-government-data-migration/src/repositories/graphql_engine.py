import json
import logging

import requests

# import logging


# GRAPHQL_URL = 'http://graphql-engine:8080/v1/graphql'
GRAPHQL_URL = "http://localhost:8080/v1/graphql"
HEADERS = {
    "x-hasura-admin-secret": "hasurapassword",
    "Content-Type": "application/json",
}


def send_graphql_request(payload: dict):
    with requests.Session() as session:
        response = session.post(
            GRAPHQL_URL,
            headers=HEADERS,
            data=json.dumps(payload)
        )

        if response.status_code != 200:
            logging.error("Request failed. Response")
            response.raise_for_status()

        responseJson = response.json()

        if 'errors' in responseJson:
            logging.error("GraphQL error:\n" + json.dumps(responseJson))
            logging.error("Failed request payload:")
            logging.error(payload)

        return responseJson


def insert_legislative_member(legislative_memeber: dict):
    query = """\
        mutation (
            $id: String,
            $bioguide: String,
            $govtrack: Int,
            $lis: String,
            $address: String,
            $bio_url: String,
            $birthday: date,
            $contact_form_url: String,
            $first_name: String,
            $last_name: String,
            $official_full: String,
            $gender: String,
            $isHouseMember: Boolean,
            $isSenateMember: Boolean,
            $party: String,
            $phone: String,
            $state: String,
            $state_rank: String,
            $terms: jsonb,
            $leadership_roles: jsonb,
            $family: jsonb,
            $other_names: jsonb
        ) {
            insert_legislative_members(objects: {
                id: $id,
                lis: $lis,
                party: $party,
                phone: $phone,
                state: $state,
                terms: $terms,
                gender: $gender,
                bio_url: $bio_url,
                address: $address,
                bioguide: $bioguide,
                birthday: $birthday,
                govtrack: $govtrack,
                state_rank: $state_rank,
                first_name: $first_name,
                last_name: $last_name,
                isHouseMember: $isHouseMember,
                official_full: $official_full,
                isSenateMember: $isSenateMember,
                contact_form_url: $contact_form_url,
                leadership_roles: $leadership_roles,
                family: $family,
                other_names: $other_names
            }, on_conflict: {
                constraint: legislative_members_pkey,
                update_columns: [
                    address, bio_url, birthday,
                    contact_form_url, first_name, last_name,
                    official_full, gender, isHouseMember,
                    party, phone, state,
                    state_rank, terms, updated_at, lis, bioguide, govtrack,
                    isSenateMember, leadership_roles, family, other_names
                ]
            })
            {
                returning {
                    id
                }
            }
        }
    """

    payload = {"query": query, "variables": legislative_memeber}

    return send_graphql_request(payload)


def insert_vote(vote: dict):
    query = """\
        mutation insert_votes_one(
            $id: String,
            $member_id: String,
            $bill_id: String,
            $decision: String
        ) {
            insert_votes_one(object: {
                id: $id,
                member_id: $member_id,
                bill_id: $bill_id,
                decision: $decision
            }) {
                id
            }
        }
    """

    payload = {"query": query, "variables": vote}

    return send_graphql_request(payload)


def insert_bill(bill: dict):
    query = """\
    mutation insert_bills_one(
        $actions: jsonb = "",
        $by_request: jsonb = "",
        $congress: String = "",
        $id: String = "",
        $introduced_at: timestamptz = "",
        $number: Int = 10,
        $sponsor: String = "",
        $status: String = "",
        $status_at: timestamptz = "",
        $subject: String = "",
        $summary: String = "",
        $title: String = "",
        $type: String = "",
        $updated_at: timestamptz = ""
        ) {
    insert_bills_one(object: {
        id: $id,
        updated_at: $updated_at,
        type: $type,
        title: $title,
        summary: $summary,
        subject: $subject,
        status_at: $status_at,
        status: $status,
        sponsor: $sponsor,
        number: $number,
        introduced_at: $introduced_at,
        congress: $congress,
        by_request: $by_request,
        actions: $actions
    },
    on_conflict: {
        constraint: bills_pkey,
        update_columns: updated_at
    }) {
        id
        }
    }
    """

    payload = {"query": query, "variables": bill}

    return send_graphql_request(payload)


def insert_bill_action(action: dict):
    query = """\
        mutation (
            $id: String,
            $bill_id: String,
            $type: String,
            $code: String,
            $text: String,
            $acted_at: date,
        ) {
            insert_bill_actions(objects: {
                id: $id,
                bill_id: $bill_id,
                type: $type,
                code: $code,
                text: $text
                acted_at: $acted_at,
            }, on_conflict: {
                constraint: bill_actions_pkey,
                update_columns: [
                    bill_id, type, code,
                    text, acted_at
                ]
            })
            {
                returning {
                    id
                }
            }
        }
    """

    payload = {"query": query, "variables": action}

    return send_graphql_request(payload)


def insert_committee(committee: dict):
    query = """\
    mutation insert_committees_one(
        $id: String = "",
        $name: String = "",
        $description: String = ""
        ) {
    insert_committees_one(object: {
        id: $id,
        name: $name,
        description: $description
        },
        on_conflict: {
            constraint: committees_pkey,
            update_columns: updated_at
        }) {
            id
        }
    }
    """

    payload = {"query": query, "variables": committee}

    return send_graphql_request(payload)


def insert_amendment(amendment: dict):
    query = """\
        mutation (
            $id: String,
            $bill_id: String,
            $amendment_id: String,
            $treaty_id: String,
            $number: Int,
            $type: String,
            $chamber: String,
            $congress_id: String,
            $description: String,
            $purpose: String,
            $status: String,
            $introduced_at: timestamp,
            $updated_at: timestamptz
            $proposed_at: timestamptz,
        ) {
            insert_amendments(objects: {
                id: $id,
                type: $type,
                bill_id: $bill_id,
                amendment_id: $amendment_id,
                treaty_id: $treaty_id,
                chamber: $chamber,
                congress_id: $congress_id,
                description: $description,
                number: $number,
                purpose: $purpose,
                status: $status,
                introduced_at: $introduced_at,
                updated_at: $updated_at
                proposed_at: $proposed_at,
            }, on_conflict: {
                constraint: amendments_pkey,
                update_columns: [
                    type, amendment_id, treaty_id, chamber,
                    congress_id, description, introduced_at, number,
                    proposed_at, purpose, status, updated_at, bill_id
                ]
            })
            {
                returning {
                    id
                }
            }
        }
    """

    payload = {"query": query, "variables": amendment}

    return send_graphql_request(payload)


def insert_amendment_action(amendment: dict):
    query = """\
        mutation (
            $id: String,
            $amendment_id: String,
            $type: String,
            $code: String,
            $text: String,
            $acted_at: date,
        ) {
            insert_amendment_actions(objects: {
                id: $id,
                amendment_id: $amendment_id,
                type: $type,
                code: $code,
                text: $text
                acted_at: $acted_at,
            }, on_conflict: {
                constraint: amendment_actions_pkey,
                update_columns: [
                    amendment_id, type, code,
                    text, acted_at
                ]
            })
            {
                returning {
                    id
                }
            }
        }
    """

    payload = {"query": query, "variables": amendment}

    return send_graphql_request(payload)


def insert_amendment_cosponsorship(cosponsorship: dict):
    query = """\
        mutation (
            $id: String,
            $legislative_member_id: String,
            $amendment_id: String,
            $original_cosponsor: Boolean,
            $sponsored_at: date,
            $withdrawn_at: date
        ) {
            insert_amendment_sponsorships(objects: {
                id: $id,
                legislative_member_id: $legislative_member_id,
                amendment_id: $amendment_id,
                original_cosponsor: $original_cosponsor,
                sponsored_at: $sponsored_at,
                withdrawn_at: $withdrawn_at
            }, on_conflict: {
                constraint: amendment_sponsorships_pkey,
                update_columns: [
                    legislative_member_id, amendment_id, original_cosponsor,
                    sponsored_at, withdrawn_at
                ]
            })
            {
                returning {
                    id
                }
            }
        }
    """

    payload = {"query": query, "variables": cosponsorship}

    return send_graphql_request(payload)


def insert_bill_cosponsorship(cosponsorship: dict):
    query = """\
        mutation (
            $id: String,
            $legislative_member_id: String,
            $bill_id: String,
            $original_cosponsor: Boolean,
            $sponsored_at: date,
            $withdrawn_at: date
        ) {
            insert_bill_cosponsorships(objects: {
                id: $id,
                legislative_member_id: $legislative_member_id,
                bill_id: $bill_id,
                original_cosponsor: $original_cosponsor,
                sponsored_at: $sponsored_at,
                withdrawn_at: $withdrawn_at
            }, on_conflict: {
                constraint: bill_sponsorships_pkey,
                update_columns: [
                    legislative_member_id, bill_id, original_cosponsor,
                    sponsored_at, withdrawn_at
                ]
            })
            {
                returning {
                    id
                }
            }
        }
    """

    payload = {"query": query, "variables": cosponsorship}

    return send_graphql_request(payload)


def insert_bill_subjects(bill_subject: dict):
    query = """\
        mutation (
            $value: String,
            $comment: String
        ) {
            insert_bill_subjects(objects: {
                value: $value,
                comment: $comment
            }, on_conflict: {
                constraint: bill_subjects_pkey,
                update_columns: [
                    comment
                ]
            })
            {
                returning {
                    value
                }
            }
        }
    """

    payload = {"query": query, "variables": bill_subject}

    return send_graphql_request(payload)


def insert_member(member: dict):
    query = """
    mutation insert_members_one(
        $id: String = "",
        $preferred_name: String = "",
        $first_name: String = "",
        $last_name: String = "",
        $gender: String = "",
        $state: String = "",
        $is_government_official: Boolean = false,
        $political_party_id: String = "",
        $image_url: String = "",
        $born_at: timestamptz = "",
        $updated_at: timestamptz = ""
        ) {
    insert_members_one(object: {
        id: $id,
        preferred_name: $preferred_name,
        first_name: $first_name,
        last_name: $last_name,
        gender: $gender,
        state: $state,
        is_government_official: $is_government_official,
        political_party_id: $political_party_id,
        image_url: $image_url,
        born_at: $born_at,
        updated_at: $updated_at
    },
    on_conflict: {
        constraint: members_pkey,
        update_columns: updated_at
    }) {
            id
        }
    }
    """

    payload = {"query": query, "variables": member}

    return send_graphql_request(payload)


def insert_elected_official(member: dict):
    query = """
    mutation insert_elected_officials_one(
        $id: String = "",
        $is_active: Boolean = false,
        $member_id: String = "",
        $position: String = "",
        $rank: String = "",
        $state: String = "",
        $political_party_id: String = "",
        $senate_terms: Int = 0,
        $house_terms: Int = 0,
        $district: Int = "",
        $description: String = "",
        $service_start_at: timestamptz = "",
        $service_end_at: timestamptz = ""
        $updated_at: timestamptz = ""
        ) {
    insert_elected_officials_one(object: {
        id: $id,
        is_active: $is_active,
        member_id: $member_id,
        position: $position,
        rank: $rank,
        state: $state,
        political_party_id: $political_party_id,
        senate_terms: $senate_terms,
        house_terms: $house_terms,
        district: $district,
        description: $description,
        service_start_at: $service_start_at,
        service_end_at: $service_end_at,
        updated_at: $updated_at
    },
    on_conflict: {
        constraint: elected_officials_pkey,
        update_columns: updated_at
    }) {
            id
        }
    }
    """

    payload = {"query": query, "variables": member}

    return send_graphql_request(payload)
