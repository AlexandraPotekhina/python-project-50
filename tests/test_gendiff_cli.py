import sys
from subprocess import check_output
from gendiff.scripts.gendiff import parse_arguments


def test_parse_arguments():
    sys.argv = ['genfiff', '--format', 'json', 'flat1.json', 'flat2.json']
    args = parse_arguments()
    assert args.first_file == 'flat1.json'
    assert args.second_file == 'flat2.json'
    assert args.format == 'json'


def test_gendiff_cli():
    with open('tests/fixtures/help_output.txt') as file:
        expected = file.read()
    result = check_output(['gendiff', '-h'], text=True)
    assert result == expected