from gendiff import generate_diff


def test_diff_plain_json():
    expected_path = 'tests/fixtures/plain_json_result.txt'
    dict_1_path = 'tests/fixtures/file1.json'
    dict_2_path = 'tests/fixtures/file2.json'

    with open(expected_path, 'r') as file:
        expected = file.read()

    result = generate_diff(dict_1_path, dict_2_path)

    assert result == expected


def test_diff_plain_yml():
    expected_path = 'tests/fixtures/plain_json_result.txt'
    dict_1_path = 'tests/fixtures/file1.yml'
    dict_2_path = 'tests/fixtures/file2.yml'

    with open(expected_path, 'r') as file:
        expected = file.read()

    result = generate_diff(dict_1_path, dict_2_path)

    assert result == expected


def test_diff_nested():
    expected_path = 'tests/fixtures/result_nested.txt'
    dict_1_path = 'tests/fixtures/file_nested1.json'
    dict_2_path = 'tests/fixtures/file_nested2.json'

    with open(expected_path, 'r') as file:
        expected = file.read()

    result = generate_diff(dict_1_path, dict_2_path)

    assert result == expected

#  @pytest.mark.parametrize