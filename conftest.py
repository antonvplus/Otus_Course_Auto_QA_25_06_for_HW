import pytest
from http_client import HttpClient

def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='https://ya.ru', help='URL for verification')
    parser.addoption('--status_code', action='store', default=200, help='Expected status code')

@pytest.fixture(scope='function')
def check_resource(request) -> tuple[HttpClient, str]:
    return HttpClient(request.config.getoption('--url')), request.config.getoption('--status_code')

@pytest.fixture(scope='class')
def create_client_for_class(request) -> HttpClient:
    return HttpClient(request.param)
