from gendiff.constants import (ADDED, REMOVED, MODIFIED, SHARED, NESTED)


def format_value(value, depth=0, space_count=4):

    if isinstance(value, (bool, int, float)):
        return str(value).lower()
    elif isinstance(value, dict):
        return format_child(value, depth, space_count)
    elif value is None:
        return 'null'

    return value


def format_string(difference, depth=0, space_count=4):
    output = []
    indent = ' ' * (depth * space_count)

    for tag, key_list, value in difference:
        key = key_list[-1] if key_list else None
        if tag == NESTED:
            value = format_string(value, depth + 1)
            output.append(
                f"{indent}  {SHARED} {key}: {value}"
            )
        elif tag == MODIFIED:
            old_value = format_value(value[0], depth + 1)
            new_value = format_value(value[1], depth + 1)
            output.extend([
                f"{indent}  {REMOVED} {key}: {old_value}",
                f"{indent}  {ADDED} {key}: {new_value}"
            ])
        else:
            value = format_string(value, depth + 1)
            output.append(
                f"{indent}  {tag} {key}: {value}"
            )

    output.append(f"{indent}}}")

    return '{\n' + '\n'.join(output)


def format_child(child, depth=0, space_count=4):
    result = []
    indent = ' ' * (depth * space_count)

    for key, value in child.items():
        formatted_value = format_value(value, depth + 1, space_count)
        result.append(f"{indent}    {key}: {formatted_value}")

    return '{\n' + '\n'.join(result) + '\n' + indent + '}'
