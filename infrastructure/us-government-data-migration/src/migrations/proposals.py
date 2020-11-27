import logging
import json
from ..repositories import graphql_engine

logging.basicConfig(
    filename="temp/proposals.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
log = logging.getLogger("")


def from_vote_data(vote_data):
    log.info("MIGRATING PROPOSAL")

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
    ]

    for key in vote_data:
        if key not in proposal_keys:
            log.warn(
                'Missed migration of Proposal/Vote property: "'
                + key
                + '": '
                + vote_data[key]
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
        "record_modified": vote_data.get("record_modified")
        # 'votes': vote_data.get('votes')
    }

    try:
        return graphql_engine.insert_proposal(proposal)
    except Exception as error:
        log.warn(type(error))
        log.warn(error)
        log.warn(json.dumps(proposal))
