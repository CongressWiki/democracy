import json

import requests

# import logging


# GRAPHQL_URL = 'http://graphql-engine:8080/v1/graphql'
GRAPHQL_URL = "http://localhost:8080/v1/graphql"
HEADERS = {
    "x-hasura-admin-secret": "hasurapassword",
    "Content-Type": "application/json",
}


def insert_proposal(proposal):
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
                result_text: $result_text
            }, on_conflict: {
                constraint: votes_pkey,
                update_columns: [
                    category, chamber, congress, date, nomination, number,
                    question, requires, result, result_text, session,
                    source_url, subject, type, updated_at
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

    with requests.Session() as session:
        response = session.post(GRAPHQL_URL, headers=HEADERS, data=json.dumps(payload))

        if response.status_code != 200:
            return response.raise_for_status()

        return response.json()


def insert_legislative_member(proposal):
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
            $family: jsonb
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
                family: $family
            }, on_conflict: {
                constraint: legislative_members_pkey,
                update_columns: [
                    address, bio_url, birthday,
                    contact_form_url, first_name, last_name,
                    official_full, gender, isHouseMember,
                    party, phone, state,
                    state_rank, terms, updated_at, lis, bioguide, govtrack,
                    isSenateMember, leadership_roles, family
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

    with requests.Session() as session:
        response = session.post(GRAPHQL_URL, headers=HEADERS, data=json.dumps(payload))

        if response.status_code != 200:
            return response.raise_for_status()

        return response.json()


def insert_vote(vote):
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

    with requests.Session() as session:
        response = session.post(GRAPHQL_URL, headers=HEADERS, data=json.dumps(payload))

        if response.status_code != 200:
            return response.raise_for_status()

        return response.json()


def insert_bill(bill):
    query = """\
        mutation (
            $id: String,
            $introduced_at: timestamp,
            $updated_at: timestamptz,
            $official_title: String,
            $popular_title: String,
            $short_title: String,
            $titles: json,
            $subjects_top_term: String,
            $subjects: json,
            $summary: json,
            $status: String,
            $status_at: timestamptz,
            $history: json,
            $enacted_as: json,
            $sponsor: json,
            $cosponsors: json,
            $committees: json,
            $amendments: json,
            $actions: json,
            $type: String,
            $by_request: String,
            $congress: String,
            $number: String,
            $related_bills: json,
            $url: String,
            $committee_reports: json
        ) {
            insert_bills(objects: {
                id: $id,
                introduced_at: $introduced_at,
                updated_at: $updated_at,
                official_title: $official_title,
                popular_title: $popular_title,
                short_title: $short_title,
                titles: $titles,
                subjects_top_term: $subjects_top_term,
                subjects: $subjects,
                summary: $summary,
                status: $status,
                status_at: $status_at,
                history: $history,
                enacted_as: $enacted_as,
                sponsor: $sponsor,
                cosponsors: $cosponsors,
                committees: $committees,
                amendments: $amendments,
                actions: $actions,
                type: $type,
                by_request: $by_request,
                congress: $congress,
                number: $number,
                related_bills: $related_bills,
                url: $url,
                committee_reports: $committee_reports
            }, on_conflict: {
                constraint: bills_pkey,
                update_columns: [
                    introduced_at, updated_at, official_title, popular_title,
                    short_title, titles, subjects_top_term,
                    subjects, summary, status, status_at, history, enacted_as,
                    sponsor, cosponsors, committees,
                    amendments, actions, type, by_request, congress, number,
                    related_bills, url, committee_reports
                ]
            })
            {
                returning {
                    id
                    official_title
                }
            }
        }
    """

    payload = {"query": query, "variables": bill}

    with requests.Session() as session:
        response = session.post(GRAPHQL_URL, headers=HEADERS, data=json.dumps(payload))

        if response.status_code != 200:
            return response.raise_for_status()

        return response.json()


def insert_amendment(amendment):
    query = """\
        mutation (
            $id: String,
            $actions: json,
            $amends_amendment: json,
            $amends_bill: json,
            $amends_treaty: json,
            $sponsor: json,
            $number: Int,
            $amendment_type: String,
            $chamber: String,
            $congress: String,
            $description: String,
            $purpose: String,
            $status: String,
            $introduced_at: timestamp,
            $proposed_at: timestamptz,
            $status_at: timestamptz,
            $updated_at: timestamptz
        ) {
            insert_amendments(objects: {
                id: $id,
                actions: $actions,
                amendment_type: $amendment_type,
                amends_amendment: $amends_amendment,
                amends_bill: $amends_bill,
                amends_treaty: $amends_treaty,
                chamber: $chamber,
                congress: $congress,
                description: $description,
                introduced_at: $introduced_at,
                number: $number,
                proposed_at: $proposed_at,
                purpose: $purpose,
                sponsor: $sponsor,
                status: $status,
                status_at: $status_at,
                updated_at: $updated_at
            }, on_conflict: {
                constraint: amendments_pkey,
                update_columns: [
                    actions, amendment_type, amends_amendment, amends_bill,
                    amends_treaty, chamber,
                    congress, description, introduced_at, number, proposed_at,
                    purpose, sponsor, status, status_at, updated_at
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

    with requests.Session() as session:
        response = session.post(GRAPHQL_URL, headers=HEADERS, data=json.dumps(payload))

        if response.status_code != 200:
            return response.raise_for_status()

        return response.json()
