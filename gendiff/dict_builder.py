# from gendiff.constants import (ADDED, REMOVED, MODIFIED, SHARED, NESTED)


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()

    if value in [int, float]:
        return str(value)

    if value is None:
        return 'null'

    return value


def get_diff_dict(difference):
    new_dict = {}

    for tag, key, value in difference:

        if tag == 'nested':
            new_dict[key[-1]] = {'type': tag, 'value': get_diff_dict(value)}

        elif tag == 'modified':
            new_dict[key[-1]] = {'type': tag,
                                 'from': format_value(value[0]),
                                 'to': format_value(value[1])}

        else:
            new_dict[key[-1]] = {'type': tag, 'value': format_value(value)}

    return new_dict
