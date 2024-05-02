import json
from gendiff.formatters import stylish


def format_string(difference):
    diff = stylish.format_string(difference, depth=0, space_count=4)

    return json.dumps(diff)