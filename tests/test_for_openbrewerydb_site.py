import pytest
from http_client import HttpClient
from models.models_for_openbrewerydb_site import get_list_breweries_response_model, GetSingleBreweryResponseModel

site = "openbrewerydb"
client = HttpClient(site)

@pytest.mark.openbrewerydb
def test_check_get_list_all_breweries() -> None:
    response = client.get('v1/breweries')
    get_list_breweries_response_model.validate_python(response)

@pytest.mark.openbrewerydb
@pytest.mark.parametrize("brewery_id", ["ee6d39c6-092f-4623-8099-5b8643f70dbe",
                                        "6c53984f-fac1-4ea7-9c44-44e25897c71a",
                                        "45119c56-345b-4adc-b481-c5cf7bfe98c4",
                                        "08f78223-24f8-4b71-b381-ea19a5bd82df",
                                        "ae7b3174-8be8-4d53-a3a5-9b8240970eea"])
def test_check_get_single_brewery(brewery_id: str) -> None:
    response = client.get(f'v1/breweries/{brewery_id}')
    response_model = GetSingleBreweryResponseModel(**response)
    assert brewery_id == response_model.id, "The id field does not match "

@pytest.mark.openbrewerydb
@pytest.mark.parametrize("search_terms",
                         [pytest.param({'query': 'San Diego'}, id='by city'),
                          pytest.param({'query':'Germany'} , id = 'by country'),
                          pytest.param({'query':'8100 Washington Ave'}, id='by address'),
                          pytest.param({'query': '78745-1197'}, id='by postal code')])
def test_check_get_search_breweries(search_terms: dict) -> None:
    response = client.get('v1/breweries/search', params=search_terms)
    response_model = get_list_breweries_response_model.validate_python(response)
    assert all([True if search_terms else False in i for i in response_model]), "Unexpected search result"

@pytest.mark.openbrewerydb
@pytest.mark.parametrize("city",
                         [pytest.param({'by_city': 'San Diego'}, id='city: San Diego'),
                          pytest.param({'by_city':'Mount Pleasant'}, id='city: Mount Pleasant'),
                          pytest.param({'by_city':'Bend'}, id='city: Bend'),
                          pytest.param({'by_city': 'Boise'}, id='city: Boise')])
def test_check_get_list_breweries_by_city(city: dict) -> None:
    response = client.get('v1/breweries', params=city)
    response_model = get_list_breweries_response_model.validate_python(response)
    assert all([True if city else False in i for i in response_model]), "Unexpected search result"

@pytest.mark.openbrewerydb
def test_check_get_random_brewery() -> None:
    response = client.get('v1/breweries/random')
    get_list_breweries_response_model.validate_python(response)
