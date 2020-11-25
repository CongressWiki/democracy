from ..repositories import graphql_engine
import json
import logging

logging.basicConfig(
    filename="votes.log",
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)
log = logging.getLogger('')


def from_vote_data(vote_data):
    log.info("MIGRATING VOTE")

    vote_groups = vote_data.get('votes')
    proposal_id = vote_data.get('vote_id')
    log.info("proposal_id: " + proposal_id)

    NAY = 'Nay'
    NO = 'No'
    if NAY in vote_groups or NO in vote_groups:
        for vote in vote_groups.get(NAY):
            check_for_missing_vote_properties(vote)

            voter_id = vote.get('id')
            new_vote_id = proposal_id + "-" + voter_id
            insert_vote({
                'id': new_vote_id,
                'legislative_member_id': vote.get('id'),
                'proposal_id': proposal_id,
                'decision': NAY
            })

    NOT_VOTING = 'Not_Voting'
    if 'Not Voting' in vote_groups:
        for vote in vote_groups.get('Not Voting'):
            check_for_missing_vote_properties(vote)

            voter_id = vote.get('id')
            new_vote_id = proposal_id + "-" + voter_id
            insert_vote({
                'id': new_vote_id,
                'legislative_member_id': vote.get('id'),
                'proposal_id': proposal_id,
                'decision': NOT_VOTING
            })

    PRESENT = 'Present'
    if PRESENT in vote_groups:
        for vote in vote_groups.get(PRESENT):
            check_for_missing_vote_properties(vote)

            voter_id = vote.get('id')
            new_vote_id = proposal_id + "-" + voter_id
            insert_vote({
                'id': new_vote_id,
                'legislative_member_id': vote.get('id'),
                'proposal_id': proposal_id,
                'decision': PRESENT
            })

    YES = 'Yes'
    YEA = 'Yea'
    AYE = 'Aye'
    if YES in vote_groups or YEA in vote_groups or AYE in vote_groups:
        for vote in vote_groups.get(YEA):
            check_for_missing_vote_properties(vote)

            voter_id = vote.get('id')
            new_vote_id = proposal_id + "-" + voter_id
            insert_vote({
                'id': new_vote_id,
                'legislative_member_id': vote.get('id'),
                'proposal_id': proposal_id,
                'decision': YEA
            })


def check_for_missing_vote_properties(vote):
    vote_keys = [
        "id"
    ]

    for key in vote:
        if key not in vote_keys:
            log.warn('Missed migration of Vote property: "' + key + '": ' + vote[key])


def insert_vote(vote):
    try:
        return graphql_engine.insert_proposal(vote)
    except Exception as error:
        log.warn(type(error))
        log.warn(error)
        log.warn(json.dumps(vote))
