import yaml
import json


def parse_dict(filepath):
    if filepath.endswith('.yml') or filepath.endswith('.yaml'):
        with open(filepath, 'r') as file:
            parsed_dict = yaml.safe_load(file)

    if filepath.endswith('.json'):
        with open(filepath, 'r') as file:
            parsed_dict = json.load(file)

    return parsed_dict