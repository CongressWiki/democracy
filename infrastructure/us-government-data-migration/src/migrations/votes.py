from ..repositories import graphql_engine
from enum import Enum


class Decision(Enum):
    Nay = 'Nay'
    Not_Voting = 'Not_Voting'
    Present = 'Present'
    Yea = 'Yea'


def from_vote_data(vote_data):
    vote_groups = vote_data.get('votes')

    if Decision.Nay in vote_groups:
        for vote in vote_groups.get(Decision.Nay):
            graphql_engine.insert_vote({
                'legislative_member_id': vote.get('id'),
                'proposal_id': vote_data.get('vote_id'),
                'decision': Decision.Nay
            })

    if 'Not Voting' in vote_groups:
        for vote in vote_groups.get('Not Voting'):
            graphql_engine.insert_vote({
                'legislative_member_id': vote.get('id'),
                'proposal_id': vote_data.get('vote_id'),
                'decision': Decision.Not_Voting()
            })

    if Decision.Present in vote_groups:
        for vote in vote_groups.get(Decision.Present):
            graphql_engine.insert_vote({
                'legislative_member_id': vote.get('id'),
                'proposal_id': vote_data.get('vote_id'),
                'decision': Decision.Present
            })

    if Decision.Yea in vote_groups:
        for vote in vote_groups.get(Decision.Yea):
            graphql_engine.insert_vote({
                'legislative_member_id': vote.get('id'),
                'proposal_id': vote_data.get('vote_id'),
                'decision': Decision.Yea
            })
