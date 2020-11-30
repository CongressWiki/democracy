import json
import logging

from ..repositories import graphql_engine


def from_vote_data(vote_data):
    logging.debug("MIGRATING PROPOSAL")

    proposal_keys = [
        "vote_id",
        "category",
        "chamber",
        "congress",
        "date",
        "number",
        "question",
        "requires",
        "result",
        "result_text",
        "session",
        "source_url",
        "subject",
        "type",
        "updated_at",
        "nomination",
        "record_modified",
        "votes",
        "amendment",
        "bill"
    ]

    for key in vote_data:
        if key not in proposal_keys:
            logging.warn(
                'Missed migration of Proposal/Vote property: "'
                + key
                + '": '
                + json.dumps(vote_data[key])
            )

    proposal = {
        "id": vote_data.get("vote_id"),
        "category": vote_data.get("category"),
        "chamber": vote_data.get("chamber"),
        "congress": vote_data.get("congress"),
        "date": vote_data.get("date"),
        "number": vote_data.get("number"),
        "question": vote_data.get("question"),
        "requires": vote_data.get("requires"),
        "result": vote_data.get("result"),
        "result_text": vote_data.get("result_text"),
        "session": vote_data.get("session"),
        "source_url": vote_data.get("source_url"),
        "subject": vote_data.get("subject"),
        "type": vote_data.get("type"),
        "updated_at": vote_data.get("updated_at"),
        "nomination": vote_data.get("nomination"),
        "record_modified": vote_data.get("record_modified"),
        "amendment": vote_data.get("amendment"),
        "bill": vote_data.get("bill"),
        # 'votes': vote_data.get('votes')
    }

    try:
        return graphql_engine.insert_proposal(proposal)
    except Exception as error:
        logging.warn(type(error))
        logging.warn(error)
        logging.warn(json.dumps(proposal))
