import json
import logging

from ..repositories import graphql_engine


def from_vote_data(vote_data):
    logging.debug("MIGRATING VOTE")

    vote_groups = vote_data.get("votes")
    proposal_id = vote_data.get("vote_id")

    NAY = "Nay"
    if vote_groups.get(NAY):
        for vote in vote_groups.get(NAY):
            check_for_missing_vote_properties(vote)

            voter_id = vote.get("id")
            new_vote_id = proposal_id + "-" + voter_id
            insert_vote(
                {
                    "id": new_vote_id,
                    "legislative_member_id": vote.get("id"),
                    "proposal_id": proposal_id,
                    "decision": NAY,
                }
            )

    NO = "No"
    if vote_groups.get(NO):
        for vote in vote_groups.get(NO):
            check_for_missing_vote_properties(vote)

            voter_id = vote.get("id")
            new_vote_id = proposal_id + "-" + voter_id
            insert_vote(
                {
                    "id": new_vote_id,
                    "legislative_member_id": vote.get("id"),
                    "proposal_id": proposal_id,
                    "decision": NAY,
                }
            )

    NOT_VOTING = "Not_Voting"
    if vote_groups.get("Not Voting"):
        for vote in vote_groups.get("Not Voting"):
            check_for_missing_vote_properties(vote)

            voter_id = vote.get("id")
            new_vote_id = proposal_id + "-" + voter_id
            insert_vote(
                {
                    "id": new_vote_id,
                    "legislative_member_id": vote.get("id"),
                    "proposal_id": proposal_id,
                    "decision": NOT_VOTING,
                }
            )

    PRESENT = "Present"
    if vote_groups.get(PRESENT):
        for vote in vote_groups.get(PRESENT):
            check_for_missing_vote_properties(vote)

            voter_id = vote.get("id")
            new_vote_id = proposal_id + "-" + voter_id
            insert_vote(
                {
                    "id": new_vote_id,
                    "legislative_member_id": vote.get("id"),
                    "proposal_id": proposal_id,
                    "decision": PRESENT,
                }
            )

    YEA = "Yea"
    if vote_groups.get(YEA):
        for vote in vote_groups.get(YEA):
            check_for_missing_vote_properties(vote)

            voter_id = vote.get("id")
            new_vote_id = proposal_id + "-" + voter_id
            insert_vote(
                {
                    "id": new_vote_id,
                    "legislative_member_id": vote.get("id"),
                    "proposal_id": proposal_id,
                    "decision": YEA
                }
            )

    YES = "Yes"
    if vote_groups.get(YES):
        for vote in vote_groups.get(YES):
            check_for_missing_vote_properties(vote)

            voter_id = vote.get("id")
            new_vote_id = proposal_id + "-" + voter_id
            insert_vote(
                {
                    "id": new_vote_id,
                    "legislative_member_id": vote.get("id"),
                    "proposal_id": proposal_id,
                    "decision": YEA
                }
            )

    AYE = "Aye"
    if vote_groups.get(AYE):
        for vote in vote_groups.get(AYE):
            check_for_missing_vote_properties(vote)

            voter_id = vote.get("id")
            new_vote_id = proposal_id + "-" + voter_id
            insert_vote(
                {
                    "id": new_vote_id,
                    "legislative_member_id": vote.get("id"),
                    "proposal_id": proposal_id,
                    "decision": YEA
                }
            )


def check_for_missing_vote_properties(vote):
    vote_keys = [
        "id", "display_name", "party", "state",
        "first_name", "last_name"
        ]

    for key in vote:
        if key not in vote_keys:
            logging.warn(
                'Missed migration of Vote property: "'
                + key
                + '": '
                + json.dumps(vote[key])
            )


def insert_vote(vote):
    try:
        return graphql_engine.insert_proposal(vote)
    except Exception as error:
        logging.warn(type(error))
        logging.warn(error)
        logging.warn(json.dumps(vote))
