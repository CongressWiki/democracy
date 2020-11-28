import json
import logging

from ..repositories import graphql_engine


def from_nominations_data(nomination_data):
    logging.debug("MIGRATING NOMINATION")

    nomination_keys = ["id"]

    for key in nomination_data:
        if key not in nomination_keys:
            logging.warn(
                'Missed migration of Bill property: "'
                + key
                + '": '
                + json.dumps(nomination_data[key])
            )

    nomination = {"id": nomination_data.get("nomination_id")}

    try:
        return graphql_engine.insert_nomination(nomination)
    except Exception as error:
        logging.warn(type(error))
        logging.warn(error)
        logging.warn(json.dumps(nomination))
