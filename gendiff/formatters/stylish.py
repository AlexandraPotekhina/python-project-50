from gendiff.constants import (ADDED, REMOVED, MODIFIED, SHARED, NESTED)
from itertools import chain


def format_value(value, depth=0, space_count=4):

    if isinstance(value, bool):
        return str(value).lower()

    if value in [int, float]:
      return str(value)

    if value is None:
        return 'null'

    if isinstance(value, dict):
      return format_child(value, depth, space_count)

    return value


def get_diff_dict(difference, depth=0, space_count=4):

  output = []
  indent = ' ' * (depth * space_count)

  for tag, key_list, value in difference:
  
    key = key_list[-1] if key_list else None

    if tag == 'nested':
      
      output.append(f"{indent}  {SHARED} {key}: {get_diff_dict(value, depth + 1)}")

    elif tag == 'modified':
      output.extend([f"{indent}  {REMOVED} {key}: {format_value(value[0], depth + 1)}",
                     f"{indent}  {ADDED} {key}: {format_value(value[1], depth + 1)}"])

    else:
      output.append(f"{indent}  {tag} {key}: {format_value(value, depth + 1)}")

  output.append(f"{indent}}}")

  return '{\n' + '\n'.join(output)


def format_child(child, depth=0, space_count=4):

  result = []
  indent = ' ' * (depth * space_count)

  for key, value in child.items():

    formatted_value = format_value(value, depth + 1, space_count)
    result.append(f"{indent}    {key}: {formatted_value}")

  return '{\n' + '\n'.join(result) + '\n' + indent + '}' 
