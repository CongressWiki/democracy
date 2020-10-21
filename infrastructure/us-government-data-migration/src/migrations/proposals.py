from ..repositories import graphql_engine


def from_vote_data(voteData):
    proposal = {
        'category': voteData.get('category'),
        'chamber': voteData.get('chamber'),
        'congress': voteData.get('congress'),
        'date': voteData.get('date'),
        'number': voteData.get('number'),
        'question': voteData.get('question'),
        'requires': voteData.get('requires'),
        'result': voteData.get('result'),
        'result_text': voteData.get('result_text'),
        'session': voteData.get('session'),
        'source_url': voteData.get('source_url'),
        'subject': voteData.get('subject'),
        'type': voteData.get('type'),
        'updated_at': voteData.get('updated_at'),
        'vote_id': voteData.get('vote_id'),
        'record_modified': voteData.get('record_modified')
    }

    return graphql_engine.insert_proposal(proposal)
