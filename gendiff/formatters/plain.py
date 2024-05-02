from gendiff.constants import (ADDED, REMOVED, MODIFIED, NESTED)


def format_value(value):

    if isinstance(value, (bool, int, float)):
        return str(value).lower()
    elif isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'


def format_string(difference):
    result = []

    for tag, key, value in difference:
        if tag == NESTED:
            result.append(format_string(value))
        elif tag == ADDED:
            result.append(
                f"Property '{'.'.join(key)}' was added with value: "
                f"{format_value(value)}"
            )
        elif tag == REMOVED:
            result.append(f"Property '{'.'.join(key)}' was removed")
        elif tag == MODIFIED:
            result.append(
                f"Property '{'.'.join(key)}' was updated. "
                f"From {format_value(value[0])} "
                f"to {format_value(value[1])}"
            )

    return '\n'.join(result)
