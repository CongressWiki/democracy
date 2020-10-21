from ..repositories import graphql_engine


def from_legislative_members(legislative_members):
    senate_member = {
        'id': legislative_members.get('id')
    }

    return graphql_engine.insert_senate_member(senate_member)
