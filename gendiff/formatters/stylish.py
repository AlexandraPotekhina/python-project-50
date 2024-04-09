from itertools import chain

def format_string(diff_dict, depth=0, space_count=4):
  output = []
  indent = ' ' * depth * space_count

  for dict_key, dict_value in diff_dict.items():
      output_val = dict_value.get('value')
      output_tag = dict_value.get('type')

      if output_tag == 'nested':
        nested = format_string(output_val, depth + 1, space_count)
        output.append(f"{indent}{SHARED} {dict_key}: {{\n{nested}\n{indent}}}")

      elif output_tag == '±':
        output.extend([f"{indent}{ADDED} {dict_key}: {format_child(dict_value.get('from'), depth + 1, space_count)}",
                       f"{indent}{REMOVED} {dict_key}: {format_child(dict_value.get('to'), depth + 1, space_count)}"])

      else:
        output.append(f"{indent}{output_tag} {dict_key}: {format_child(output_val, depth + 1, space_count)}")

  if depth == 0:
      return '{\n' + '\n'.join(output) + '\n}'
  else:
      return '\n'.join(output)


def format_child(child, depth=0, space_count=4):
  if not isinstance(child, dict):
    return child

  result = []
  indent = ' ' * depth * space_count

  for key, value in child.items():
        result.append(
            f"{indent}    {key}: {format_child(value, depth + 1, space_count)}"
        )
  if depth == 0:
      return '{\n' + '\n'.join(result) + '\n}'
  else:
      return '{\n' + '\n'.join(result) + '\n' + indent + '}'