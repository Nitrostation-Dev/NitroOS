import json


def get_json_data(file_path: str):
    with open(file_path) as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            raise json.JSONDecodeError("")

    return data
