from ..repositories import graphql_engine


def from_legislative_members(legislative_members):
    house_member = {
        'id': legislative_members.get('id')
    }

    return graphql_engine.insert_house_member(house_member)
