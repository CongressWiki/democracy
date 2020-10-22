from ..repositories import graphql_engine


def from_vote_data(vote_data):
    proposal = {
        'id': vote_data.get('vote_id'),
        'category': vote_data.get('category'),
        'chamber': vote_data.get('chamber'),
        'congress': vote_data.get('congress'),
        'date': vote_data.get('date'),
        'number': vote_data.get('number'),
        'question': vote_data.get('question'),
        'requires': vote_data.get('requires'),
        'result': vote_data.get('result'),
        'result_text': vote_data.get('result_text'),
        'session': vote_data.get('session'),
        'source_url': vote_data.get('source_url'),
        'subject': vote_data.get('subject'),
        'type': vote_data.get('type'),
    }

    return graphql_engine.insert_proposal(proposal)
