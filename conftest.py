import pytest
import requests


class APICall:
    def __init__(self, url):
        self.url = url

    def get_method(self, path='/', params=None):
        url = self.url + path
        return requests.get(url=url, params=params)


def pytest_addoption(parser):
    parser.addoption(
        '--url',
        choices='https://mail.ru',
        required=True,
        help='Choose resource mail.ru'
    )

    parser.addoption(
        '--status_code',
        default='200',
        choices='200',
        help='Choose status code 200',
    )


@pytest.fixture
def call_api(request):
    base_url = request.config.getoption('--url')
    return APICall(url=base_url)
