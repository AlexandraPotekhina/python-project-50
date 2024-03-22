from gendiff import generate_diff


def test_diff_plain():
    expected_path = 'tests/fixtures/plain_json_result.txt'
    dict_1_path = 'tests/fixtures/file1.json'
    dict_2_path = 'tests/fixtures/file2.json'

    with open(expected_path, 'r') as file:
        expected = file.read()

    result = generate_diff(dict_1_path, dict_2_path)

    assert result == expected


#  @pytest.mark.parametrize