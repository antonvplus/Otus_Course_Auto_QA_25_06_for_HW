from http_client import HttpClient

def test_for_fixture_check_resource(check_resource: tuple[HttpClient, str]):
    assert check_resource[0].status_code() == int(check_resource[1]), f"The server returned an unexpected response code: {check_resource[0].status_code()}"