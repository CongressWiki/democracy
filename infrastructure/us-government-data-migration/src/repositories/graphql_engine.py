import logging
import requests
import json

logging.basicConfig()
log = logging.getLogger('[graphql_engine.py]')
log.setLevel(logging.ERROR)

GRAPHQL_URL = 'http://graphql-engine:8080/v1/graphql'
HEADERS = {'x-hasura-admin-secret': 'goodpassword', "Content-Type": "application/json"}


def insert_proposal(proposal):
    query = """\
        mutation ($category: String, $chamber: String, $congress: Int, $date: timestamptz,
        $number: Int, $question: String, $requires: String, $result: String, $result_text: String, $session: String,
        $source_url: String, $subject: String, $type: String, $id: String) {
            insert_proposals(objects: {
                id: $id,
                category: $category,
                chamber: $chamber,
                congress: $congress,
                date: $date,
                number: $number,
                question: $question,
                requires: $requires,
                result: $result,
                result_text: $result_text,
                session: $session,
                source_url: $source_url,
                subject: $subject,
                type: $type
            }, on_conflict: {
                constraint: votes_pkey,
                update_columns: [
                    category, chamber, congress, date, number,
                    question, requires, result, result_text, session,
                    source_url, subject, type, updated_at
                ]
            })
            {
                returning {
                    id
                    number
                    question
                }
            }
        }
    """

    payload = {"query": query, "variables": proposal}

    with requests.Session() as session:
        log.info('Sending request to ' + GRAPHQL_URL)
        response = session.post(GRAPHQL_URL, headers=HEADERS, data=json.dumps(payload))

        if response.status_code != 200:
            response.raise_for_status()

        return response.json()


def insert_legislative_member(proposal):
    query = """\
        mutation (
            $id: String, $bioguide: String, $govtrack: Int, $lis: String,
            $address: String, $bio_url: String, $birthday: date,
            $contact_form_url: String, $first_name: String, $last_name: String,
            $official_full: String, $gender: String, $isHouseMember: Boolean,
            $isSenateMember: Boolean, $party: String, $phone: String,
            $state: String, $state_rank: String, $terms: jsonb
        ) {
            insert_legislative_members(objects: {
                id: $id,
                bioguide: $bioguide,
                govtrack: $govtrack,
                lis: $lis,
                address: $address,
                bio_url: $bio_url,
                birthday: $birthday,
                contact_form_url: $contact_form_url,
                first_name: $first_name,
                last_name: $last_name,
                official_full: $official_full,
                gender: $gender,
                isHouseMember: $isHouseMember,
                isSenateMember: $isSenateMember,
                party: $party,
                phone: $phone,
                state: $state,
                state_rank: $state_rank,
                terms: $terms
            }, on_conflict: {
                constraint: legislative_members_pkey,
                update_columns: [
                    address, bio_url, birthday,
                    contact_form_url, first_name, last_name,
                    official_full, gender, isHouseMember,
                    party, phone, state,
                    state_rank, terms, updated_at
                ]
            })
            {
                returning {
                    id
                    official_full
                    updated_at
                    created_at
                }
            }
        }
    """

    payload = {"query": query, "variables": proposal}

    with requests.Session() as session:
        log.info('GRAPHQL_URL: ' + GRAPHQL_URL)
        response = session.post(GRAPHQL_URL, headers=HEADERS, data=json.dumps(payload))

        if response.status_code != 200:
            response.raise_for_status()

        return response.json()


def insert_vote(vote):
    query = """\
        mutation (
            $legislative_member_id: String, $proposal_id: String, $decision: decisions_enum
        ) {
            insert_votes(objects: {
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
                    updated_at
                    legislative_member_id
                    proposal_id
                    decision
                }
            }
        }
    """

    payload = {"query": query, "variables": vote}

    with requests.Session() as session:
        log.info('GRAPHQL_URL: ' + GRAPHQL_URL)
        response = session.post(GRAPHQL_URL, headers=HEADERS, data=json.dumps(payload))

        if response.status_code != 200:
            response.raise_for_status()

        return response.json()


def subscribe_to_recent_proposals():
    query = """\
        subscription votes {
            proposals(limit: 10, order_by: {votes_aggregate: {count: desc}}) {
                id
                subject
                votes {
                    legislative_member {
                        official_full
                        party
                    }
                }
            }
        }
    """

    payload = {"query": query}

    with requests.Session() as session:
        log.info('GRAPHQL_URL: ' + GRAPHQL_URL)
        response = session.post(GRAPHQL_URL, headers=HEADERS, data=json.dumps(payload))

        if response.status_code != 200:
            response.raise_for_status()

        return response.json()


def subscribe_to_votes_by_legislative_member():
    query = """\
        subscription votes {
            legislative_members(limit: 3) {
                official_full
                votes_aggregate(distinct_on: decision) {
                    nodes {
                        decisionByDecision {
                            value
                            votes_aggregate {
                                aggregate {
                                    count
                                }
                            }
                        }
                    }
                }
            }
        }
    """

    payload = {"query": query}

    with requests.Session() as session:
        log.info('GRAPHQL_URL: ' + GRAPHQL_URL)
        response = session.post(GRAPHQL_URL, headers=HEADERS, data=json.dumps(payload))

        if response.status_code != 200:
            response.raise_for_status()

        return response.json()
