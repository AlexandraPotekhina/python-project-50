from gendiff.parser import parse_dict
from gendiff.formatters import get_formatter
from gendiff.dict_builder import get_diff_dict
from gendiff.constants import (ADDED, REMOVED, MODIFIED, SHARED, NESTED)


def get_diff(dict1, dict2, node=[]):

    # def walk(object1, object2, node=[]):

        for key in sorted(dict1.keys() | dict2.keys()):
            val1, val2 = dict1.get(key, object()), dict2.get(key, object())
            new_node = node + [key]

            if isinstance(val1, dict) and isinstance(val2, dict):
                diffs = list(get_diff(val1, val2, new_node))  
                if diffs: 
                    yield NESTED, new_node, diffs
            elif key not in dict2:
                yield REMOVED, new_node, val1
            elif key not in dict1:
                yield ADDED, new_node, val2
            elif val1 == val2:
                yield SHARED, new_node, val2
            elif val1 != val2:
                yield MODIFIED, new_node, (val1, val2)

    # return walk(dict1, dict2)


def generate_diff(file1, file2, formatter_style='stylish'):
    file1 = parse_dict(file1)
    file2 = parse_dict(file2)

    diff = get_diff(file1, file2)

    diff_dict = get_diff_dict(diff)

    formatter = get_formatter(formatter_style)

    return formatter(diff_dict)
