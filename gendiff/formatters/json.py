import json
from gendiff.constants import (ADDED, REMOVED, MODIFIED, SHARED, NESTED)


def get_diff_dict(difference):

    new_dict = {}

    for tag, key, value in difference:
        if tag == NESTED:
            new_dict[key[-1]] = get_diff_dict(value)
        elif tag == MODIFIED:
            new_dict[key[-1]] = {
                'type': tag,
                'old_value': value[0],
                'new_value': value[1]
            }
        elif tag == ADDED:
            new_dict[key[-1]] = {
                'type': 'added',
                'new_value': value
            }
        elif tag == REMOVED:
            new_dict[key[-1]] = {
                'type': 'removed',
                'old_value': value
            }
        elif tag == SHARED:
            new_dict[key[-1]] = value
            
    return new_dict


def format_string(difference):
    diff = get_diff_dict(difference)

    return json.dumps(diff, indent=2)