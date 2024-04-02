from gendiff.parser import parse_dict


ADDED = '+'
REMOVED = '-'
MODIFIED = '±' 
SHARED = ' '


def format_value(value):
    if isinstance(value, (bool, type(None))):
        return str(value).lower()

    return str(value)


def format_dict_item(key, tag, value):
  
    if tag == MODIFIED:
        return [f"  - {key}: {format_value(value[0])}", 
                f"  + {key}: {format_value(value[1])}"]
    
    return [f"  {tag} {key}: {format_value(value)}"]


def gen_diff_string(diff_list):

    return '{\n' + '\n'.join(diff_list) + '\n}'


def get_diff(object1, object2):
        
    for key in sorted(object1 | object2):
        val1, val2 = object1.get(key, object()), object2.get(key, object())

        if key not in object2:
            yield REMOVED, key, val1

        elif key not in object1:
            yield ADDED, key, val2

        elif val1 == val2:
            yield SHARED, key, val2

        elif val1 != val2:
            yield MODIFIED, key, (val1, val2)


def format_diff(dict1, dict2):
  
    for difference in get_diff(dict1, dict2):
        yield from format_dict_item(difference)


def gen_diff(file1, file2):

    file1 = parse_dict(file1)
    file1 = parse_dict(file2)

    diff = format_diff(file1, file2)

    return gen_diff_string(diff)
