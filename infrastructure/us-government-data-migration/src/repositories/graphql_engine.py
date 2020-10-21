import logging
import requests
import json

logging.basicConfig()
log = logging.getLogger('[graphql_engine.py]')
log.setLevel(logging.DEBUG)

GRAPHQL_URL = 'http://graphql-engine:8080/v1/graphql'
HEADERS = {'x-hasura-admin-secret': 'goodpassword', "Content-Type": "application/json"}


def insert_proposal(proposal):
    query = """\
        mutation ($category: String, $chamber: String, $congress: Int, $date: timestamptz,
        $number: Int, $question: String, $requires: String, $result: String, $result_text: String, $session: String,
        $source_url: String, $subject: String, $type: String, $updated_at: timestamptz, $vote_id: String,
        $record_modified: timestamptz) {
            insert_proposals(objects: {
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
                type: $type,
                updated_at: $updated_at,
                id: $vote_id,
                vote_id: $vote_id,
                record_modified: $record_modified
            }, on_conflict: {constraint: votes_pkey, update_columns: [category, chamber, congress, date, number,
            question, requires, result, result_text, session, source_url, subject, type, updated_at, record_modified]})
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
        log.info('GRAPHQL_URL: ' + GRAPHQL_URL)
        response = session.post(GRAPHQL_URL, headers=HEADERS, data=json.dumps(payload))

        if response.status_code != 200:
            response.raise_for_status()

        return response.json()


def insert_senate_member(proposal):
    query = """\
        mutation ($category: String, $chamber: String, $congress: Int, $date: timestamptz,
        $number: Int, $question: String, $requires: String, $result: String, $result_text: String, $session: String,
        $source_url: String, $subject: String, $type: String, $updated_at: timestamptz, $vote_id: String,
        $record_modified: timestamptz) {
            insert_proposals(objects: {
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
                type: $type,
                updated_at: $updated_at,
                id: $vote_id,
                vote_id: $vote_id,
                record_modified: $record_modified
            }, on_conflict: {constraint: votes_pkey, update_columns: [category, chamber, congress, date, number,
            question, requires, result, result_text, session, source_url, subject, type, updated_at, record_modified]})
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
        log.info('GRAPHQL_URL: ' + GRAPHQL_URL)
        response = session.post(GRAPHQL_URL, headers=HEADERS, data=json.dumps(payload))

        if response.status_code != 200:
            response.raise_for_status()

        return response.json()


def insert_house_member(proposal):
    query = """\
        mutation ($category: String, $chamber: String, $congress: Int, $date: timestamptz,
        $number: Int, $question: String, $requires: String, $result: String, $result_text: String, $session: String,
        $source_url: String, $subject: String, $type: String, $updated_at: timestamptz, $vote_id: String,
        $record_modified: timestamptz) {
            insert_proposals(objects: {
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
                type: $type,
                updated_at: $updated_at,
                id: $vote_id,
                vote_id: $vote_id,
                record_modified: $record_modified
            }, on_conflict: {constraint: votes_pkey, update_columns: [category, chamber, congress, date, number,
            question, requires, result, result_text, session, source_url, subject, type, updated_at, record_modified]})
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
        log.info('GRAPHQL_URL: ' + GRAPHQL_URL)
        response = session.post(GRAPHQL_URL, headers=HEADERS, data=json.dumps(payload))

        if response.status_code != 200:
            response.raise_for_status()

        return response.json()
