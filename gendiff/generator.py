import json


def format_value(value):
    if isinstance(value, (bool, type(None))):
        return str(value).lower()

    return str(value)


def format_dict_item(key, value, sign):
    formatted_value = format_value(value)
    return f"  {sign} {key}: {formatted_value}"


def get_diff(dict1, dict2):

    diff = []
    all_keys = set(dict1.keys()) | set(dict2.keys())

    for key in sorted(all_keys):
        file1_value = dict1.get(key, None)
        file2_value = dict2.get(key, None)

        if key not in dict2:
            diff.append(format_dict_item(key, file1_value, '-'))  # removed

        elif key not in dict1:
            diff.append(format_dict_item(key, file2_value, '+'))  # added

        elif file1_value != file2_value:
            diff.append(format_dict_item(key, file1_value, '-'))
            diff.append(format_dict_item(key, file2_value, '+'))

        else:
            diff.append(format_dict_item(key, file2_value, ' '))  # shared

    return diff


def gen_diff_string(diff_list):

    return '{\n' + '\n'.join(diff_list) + '\n}'


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))

    diff = get_diff(file1, file2)

    return gen_diff_string(diff)
