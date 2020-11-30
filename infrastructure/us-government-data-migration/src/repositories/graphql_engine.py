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

        return responseJson


def insert_proposal(proposal: dict):
    query = """\
        mutation (
            $number: Int,
            $congress: Int,
            $date: timestamptz,
            $updated_at: timestamp,
            $record_modified: timestamp,
            $nomination: json,
            $id: String,
            $type: String,
            $result: String,
            $session: String,
            $chamber: String,
            $subject: String,
            $category: String,
            $question: String,
            $requires: String,
            $source_url: String,
            $result_text: String,
            $amendment: jsonb,
            $bill: jsonb
        ) {
            insert_proposals(objects: {
                number: $number,
                congress: $congress,
                date: $date,
                updated_at: $updated_at,
                nomination: $nomination,
                id: $id,
                type: $type,
                result: $result,
                session: $session,
                chamber: $chamber,
                subject: $subject,
                category: $category,
                question: $question,
                requires: $requires,
                source_url: $source_url,
                result_text: $result_text,
                amendment: $amendment,
                bill: $bill
            }, on_conflict: {
                constraint: votes_pkey,
                update_columns: [
                    category, chamber, congress, date, nomination, number,
                    question, requires, result, result_text, session,
                    source_url, subject, type, updated_at, amendment, bill
                ]
            })
            {
                returning {
                    id
                }
            }
        }
    """

    payload = {"query": query, "variables": proposal}

    return send_graphql_request(payload)


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
        mutation (
            $id: String,
            $legislative_member_id: String,
            $proposal_id: String,
            $decision: decisions_enum
        ) {
            insert_votes(objects: {
                id: $id,
                legislative_member_id: $legislative_member_id,
                proposal_id: $proposal_id,
                decision: $decision
            }, on_conflict: {
                constraint: votes_pkey1,
                update_columns: [
                    updated_at, legislative_member_id, proposal_id,
                    decision
                ]
            })
            {
                returning {
                    id
                }
            }
        }
    """

    payload = {"query": query, "variables": vote}

    return send_graphql_request(payload)


def insert_bill(bill: dict):
    query = """\
        mutation (
            $id: String,
            $introduced_at: timestamp,
            $updated_at: timestamptz,
            $title: String,
            $subject: String,
            $summary: String,
            $status: String,
            $type: String,
            $by_request: Boolean,
            $number: String,
            $congress_id: String,
            $sponsor_id: String
        ) {
            insert_bills(objects: {
                id: $id,
                introduced_at: $introduced_at,
                updated_at: $updated_at,
                title: $title,
                subject: $subject,
                summary: $summary,
                status: $status,
                type: $type,
                by_request: $by_request,
                number: $number,
                congress_id: $congress_id,
                sponsor_id: $sponsor_id
            }, on_conflict: {
                constraint: bills_pkey,
                update_columns: [
                    introduced_at, updated_at, title, subject,
                    summary, status, type, by_request, number,
                    congress_id, sponsor_id
                ]
            })
            {
                returning {
                    id
                }
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
        mutation (
            $id: String,
            $name: String
        ) {
            insert_committees(objects: {
                id: $id,
                name: $name
            }, on_conflict: {
                constraint: committees_pkey,
                update_columns: [
                    name
                ]
            })
            {
                returning {
                    id
                }
            }
        }
    """

    payload = {"query": query, "variables": committee}

    return send_graphql_request(payload)


def insert_committee_has_bill(committee_has_bill: dict):
    query = """\
        mutation (
            $committee_id: String,
            $bill_id: String
        ) {
            insert_committee_has_bill(objects: {
                committee_id: $id,
                bill_id: $name
            })
            {
                returning {
                    committee_id,
                    bill_id
                }
            }
        }
    """

    payload = {"query": query, "variables": committee_has_bill}

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
