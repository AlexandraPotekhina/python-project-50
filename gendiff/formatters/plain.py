def format_value_plain(value):

    if isinstance(value, bool):
        return str(value).lower()
    if value in [int, float]:
        return str(value)
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return f"[complex value]"
    
    return value


def format_string(difference):
    result = []

    for tag, key, value in difference:
        if tag == 'nested':
            result.append(format_string(value))
        elif tag == '+':
            result.append(f"Property '{'.'.join(key)}' was added with value: '{format_value_plain(value)}'")
        elif tag == '-':
            result.append(f"Property '{'.'.join(key)}' was removed")
        elif tag == 'modified':
            result.append(f"Property '{'.'.join(key)}' was updated. From '{format_value_plain(value[0])}' to '{format_value_plain(value[1])}'")
    
    return '\n'.join(result)