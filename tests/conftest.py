import pytest
import json


@pytest.fixture
def file1():
    return json.load(open('tests/fixtures/file1.json'))


@pytest.fixture
def file2():
    return json.load(open('tests/fixtures/file2.json'))