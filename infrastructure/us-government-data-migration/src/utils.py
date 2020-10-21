import json


def read_json_file(path):
    with open(path) as file:
        return json.load(file)
