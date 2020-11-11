from ..repositories import graphql_engine
import logging

logging.basicConfig()
log = logging.getLogger('[votes.py]')
log.setLevel(logging.DEBUG)


def from_vote_data(vote_data):
    vote_groups = vote_data.get('votes')

    log.info("NEW VOTE")

    NAY = 'Nay'
    if NAY in vote_groups:
        for vote in vote_groups.get(NAY):
            graphql_engine.insert_vote({
                'legislative_member_id': vote.get('id'),
                'proposal_id': vote_data.get('vote_id'),
                'decision': NAY
            })

    NOT_VOTING = 'Not_Voting'
    if 'Not Voting' in vote_groups:
        for vote in vote_groups.get('Not Voting'):
            graphql_engine.insert_vote({
                'legislative_member_id': vote.get('id'),
                'proposal_id': vote_data.get('vote_id'),
                'decision': NOT_VOTING
            })

    PRESENT = 'Present'
    if PRESENT in vote_groups:
        for vote in vote_groups.get(PRESENT):
            graphql_engine.insert_vote({
                'legislative_member_id': vote.get('id'),
                'proposal_id': vote_data.get('vote_id'),
                'decision': PRESENT
            })

    YEA = 'Yea'
    if YEA in vote_groups:
        for vote in vote_groups.get(YEA):
            graphql_engine.insert_vote({
                'legislative_member_id': vote.get('id'),
                'proposal_id': vote_data.get('vote_id'),
                'decision': YEA
            })
