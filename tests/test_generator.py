import pytest
from gendiff import generate_diff

@pytest.mark.parametrize("path1, path2, expected_result, output_format", [
     ('tests/fixtures/flat1.json', 'tests/fixtures/flat2.json', 'tests/fixtures/diff_flat_stylish.txt', None),
     ('tests/fixtures/flat1.yml', 'tests/fixtures/flat2.yml', 'tests/fixtures/diff_flat_stylish.txt', None),
     ('tests/fixtures/nested1.json', 'tests/fixtures/nested2.json', 'tests/fixtures/diff_nested_stylish.txt', None),
     ('tests/fixtures/nested1.yml', 'tests/fixtures/nested2.yml', 'tests/fixtures/diff_nested_stylish.txt', None),
     ('tests/fixtures/flat1.json', 'tests/fixtures/flat2.json', 'tests/fixtures/diff_flat_plain.txt', 'plain'),
     ('tests/fixtures/flat1.yml', 'tests/fixtures/flat2.yml', 'tests/fixtures/diff_flat_plain.txt', 'plain'),
     ('tests/fixtures/nested1.json', 'tests/fixtures/nested2.json', 'tests/fixtures/diff_nested_plain.txt', 'plain'),
     ('tests/fixtures/nested1.yml', 'tests/fixtures/nested2.yml', 'tests/fixtures/diff_nested_plain.txt', 'plain'),
     ('tests/fixtures/flat1.json', 'tests/fixtures/flat2.json', 'tests/fixtures/diff_flat.json', 'json'),
     ('tests/fixtures/flat1.yml', 'tests/fixtures/flat2.yml', 'tests/fixtures/diff_flat.json', 'json'),
     ('tests/fixtures/nested1.json', 'tests/fixtures/nested2.json', 'tests/fixtures/diff_nested.json', 'json'),
     ('tests/fixtures/nested1.yml', 'tests/fixtures/nested2.yml', 'tests/fixtures/diff_nested.json', 'json')
 ])


def test_generate_diff(path1, path2, expected_result, output_format):
    
    with open(expected_result, 'r') as file:
        expected = file.read()

    result = generate_diff(path1, path2, output_format)

    assert result == expected
