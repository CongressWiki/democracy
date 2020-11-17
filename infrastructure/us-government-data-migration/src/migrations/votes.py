from ..repositories import graphql_engine
import logging

logging.basicConfig()
log = logging.getLogger('[votes.py]')
log.setLevel(logging.DEBUG)


def from_vote_data(vote_data):
    vote_groups = vote_data.get('votes')

    log.info("NEW VOTE")

    proposal_id = vote_data.get('vote_id')
    log.info("proposal_id: " + proposal_id)

    NAY = 'Nay'
    if NAY in vote_groups:
        for vote in vote_groups.get(NAY):
            voter_id = vote.get('id')
            log.info("voter_id: " + voter_id)
            id = proposal_id + "-" + voter_id
            log.info('id: ' + id)
            graphql_engine.insert_vote({
                'id': id,
                'legislative_member_id': vote.get('id'),
                'proposal_id': vote_data.get('vote_id'),
                'decision': NAY
            })

    NOT_VOTING = 'Not_Voting'
    if 'Not Voting' in vote_groups:
        for vote in vote_groups.get('Not Voting'):
            voter_id = vote.get('id')
            log.info("voter_id: " + voter_id)
            id = proposal_id + "-" + voter_id
            log.info('id: ' + id)
            graphql_engine.insert_vote({
                'id': id,
                'legislative_member_id': vote.get('id'),
                'proposal_id': vote_data.get('vote_id'),
                'decision': NOT_VOTING
            })

    PRESENT = 'Present'
    if PRESENT in vote_groups:
        for vote in vote_groups.get(PRESENT):
            voter_id = vote.get('id')
            log.info("voter_id: " + voter_id)
            id = proposal_id + "-" + voter_id
            log.info('id: ' + id)
            graphql_engine.insert_vote({
                'id': id,
                'legislative_member_id': vote.get('id'),
                'proposal_id': vote_data.get('vote_id'),
                'decision': PRESENT
            })

    YEA = 'Yea'
    if YEA in vote_groups:
        for vote in vote_groups.get(YEA):
            voter_id = vote.get('id')
            log.info("voter_id: " + voter_id)
            id = proposal_id + "-" + voter_id
            log.info('id: ' + id)
            graphql_engine.insert_vote({
                'id': id,
                'legislative_member_id': vote.get('id'),
                'proposal_id': vote_data.get('vote_id'),
                'decision': YEA
            })
