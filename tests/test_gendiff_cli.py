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