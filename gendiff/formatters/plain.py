def format_value_plain(value):

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
        if tag == 'nested':
            result.append(format_string(value))
        elif tag == '+':
            result.append(
                f"Property '{'.'.join(key)}' was added with value: "
                f"{format_value_plain(value)}"
            )
        elif tag == '-':
            result.append(f"Property '{'.'.join(key)}' was removed")
        elif tag == 'modified':
            result.append(
                f"Property '{'.'.join(key)}' was updated. "
                f"From {format_value_plain(value[0])} "
                f"to {format_value_plain(value[1])}"
            )

    return '\n'.join(result)
