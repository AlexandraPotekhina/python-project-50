from gendiff import generate_diff


def test_diff_plain():
    expected = 'tests/fixtures/plain_json_result.txt'
    result = generate_diff('tests/fixtures/file1.json',
                           'tests/fixtures/file2.json')
    assert result == expected


#  @pytest.mark.parametrize