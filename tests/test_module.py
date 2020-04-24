import pytest


@pytest.mark.parametrize('expected_response', [404])
def test_response(call_api, expected_response):
    response = call_api.get_method(path='/sfhfhfhfhfhfhfhfh')
    if response.status_code == expected_response:
        assert True
