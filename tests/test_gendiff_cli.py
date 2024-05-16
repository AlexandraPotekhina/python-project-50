import sys
import subprocess 
from gendiff.scripts.gendiff import parse_arguments


def test_parse_arguments():
    sys.argv = ['gendiff', '--format', 'json', 'flat1.json', 'flat2.json']
    args = parse_arguments()
    assert args.first_file == 'flat1.json'
    assert args.second_file == 'flat2.json'
    assert args.format == 'json'


def test_gendiff_cli():
    with open('tests/fixtures/help_output.txt', 'r') as file:
        expected = file.read()
    result = subprocess.run(['gendiff', '-h'], capture_output=True, text=True)
    assert result.stdout.rstrip() == expected

    with open('tests/fixtures/diff_flat_stylish.txt') as file:
        expected = file.read()
    result = subprocess.run(['gendiff', 'tests/fixtures/flat1.json', 'tests/fixtures/flat2.json'], capture_output=True, text=True)
    assert result.stdout.rstrip() == expected

    with open('tests/fixtures/diff_flat_stylish.txt') as file:
        expected = file.read()
    result = subprocess.run(['gendiff', 'tests/fixtures/flat1.json', 'tests/fixtures/flat2.json', '-f', 'stylish'], capture_output=True, text=True)
    assert result.stdout.rstrip() == expected

    with open('tests/fixtures/diff_flat_plain.txt') as file:
        expected = file.read()
    result = subprocess.run(['gendiff', 'tests/fixtures/flat1.json', 'tests/fixtures/flat2.json', '-f', 'plain'], capture_output=True, text=True)
    assert result.stdout.rstrip() == expected

    with open('tests/fixtures/diff_flat.json') as file:
        expected = file.read()
    result = subprocess.run(['gendiff', 'tests/fixtures/flat1.json', 'tests/fixtures/flat2.json', '-f', 'json'], capture_output=True, text=True)
    assert result.stdout.rstrip() == expected

    with open('tests/fixtures/diff_nested_stylish.txt') as file:
        expected = file.read()
    result = subprocess.run(['gendiff', 'tests/fixtures/nested1.json', 'tests/fixtures/nested2.json'], capture_output=True, text=True)
    assert result.stdout.rstrip() == expected

    with open('tests/fixtures/diff_nested_stylish.txt') as file:
        expected = file.read()
    result = subprocess.run(['gendiff', 'tests/fixtures/nested1.json', 'tests/fixtures/nested2.json', '-f', 'stylish'], capture_output=True, text=True)
    assert result.stdout.rstrip() == expected

    with open('tests/fixtures/diff_nested_plain.txt') as file:
        expected = file.read()
    result = subprocess.run(['gendiff', 'tests/fixtures/nested1.json', 'tests/fixtures/nested2.json', '-f', 'plain'], capture_output=True, text=True)
    assert result.stdout.rstrip() == expected

    with open('tests/fixtures/diff_nested.json') as file:
        expected = file.read()
    result = subprocess.run(['gendiff', 'tests/fixtures/nested1.json', 'tests/fixtures/nested2.json', '-f', 'json'], capture_output=True, text=True)
    assert result.stdout.rstrip() == expected
