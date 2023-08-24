import json


def get_json_data(file_path: str):
    with open(file_path) as file:
        data = json.load(file)

    return data
