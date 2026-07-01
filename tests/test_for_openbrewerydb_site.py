import pytest
from http_client import HttpClient
from models.models_for_openbrewerydb_site import get_list_breweries_response_model, GetSingleBreweryResponseModel
from service.services_for_openbrewerydb import (check_response_list_all_breweries, check_response_single_brewery,
                                                check_response_list_found_breweries, check_response_random_brewery)

@pytest.mark.parametrize('create_client_for_class', ['https://api.openbrewerydb.org'], indirect=True)
class TestOpenBreweryDBSite:

    @pytest.mark.openbrewerydb
    def test_check_get_list_all_breweries(self, create_client_for_class: HttpClient) -> None:
        response = create_client_for_class.get('v1/breweries')
        response_from_check_func = check_response_list_all_breweries(get_list_breweries_response_model.validate_python(response))
        assert response_from_check_func[0], response_from_check_func[1]

    @pytest.mark.openbrewerydb
    @pytest.mark.parametrize("brewery_id", ["ee6d39c6-092f-4623-8099-5b8643f70dbe",
                                            "6c53984f-fac1-4ea7-9c44-44e25897c71a",
                                            "45119c56-345b-4adc-b481-c5cf7bfe98c4",
                                            "08f78223-24f8-4b71-b381-ea19a5bd82df",
                                            "ae7b3174-8be8-4d53-a3a5-9b8240970eea"])

    def test_check_get_single_brewery(self, create_client_for_class: HttpClient, brewery_id: str) -> None:
        response = create_client_for_class.get(f'v1/breweries/{brewery_id}')
        response_model = GetSingleBreweryResponseModel(**response)
        response_from_check_func = check_response_single_brewery(response_model, brewery_id)
        assert response_from_check_func[0], response_from_check_func[1]

    @pytest.mark.openbrewerydb
    @pytest.mark.parametrize("search_terms",
                             [pytest.param({'query': 'San Diego'}, id='by city'),
                              pytest.param({'query': 'Germany'}, id='by country'),
                              pytest.param({'query': '5164 Kennedy Ave'}, id='by address'),
                              pytest.param({'query': '5138368733'}, id='by phone number')])
    def test_check_get_search_breweries(self, create_client_for_class: HttpClient, search_terms: dict) -> None:
        response = create_client_for_class.get('v1/breweries/search', params=search_terms)
        response_model = get_list_breweries_response_model.validate_python(response)
        response_from_check_func = check_response_list_found_breweries(response_model)
        assert response_from_check_func[0], response_from_check_func[1]
        assert all(search_terms['query'] in (i.city, i.country, i.street, i.phone) for i in response_model), "Unexpected search result"

    @pytest.mark.openbrewerydb
    @pytest.mark.parametrize("city",
                             [pytest.param({'by_city': 'San Diego'}, id='city: San Diego'),
                              pytest.param({'by_city': 'Mount Pleasant'}, id='city: Mount Pleasant'),
                              pytest.param({'by_city': 'Bend'}, id='city: Bend'),
                              pytest.param({'by_city': 'Boise'}, id='city: Boise')])
    def test_check_get_list_breweries_by_city(self, create_client_for_class: HttpClient, city: dict) -> None:
        response = create_client_for_class.get('v1/breweries', params=city)
        response_model = get_list_breweries_response_model.validate_python(response)
        response_from_check_func = check_response_list_found_breweries(response_model)
        assert response_from_check_func[0], response_from_check_func[1]
        assert all(city['by_city'] in i.city for i in response_model), "Unexpected search result"

    @pytest.mark.openbrewerydb
    def test_check_get_random_brewery(self, create_client_for_class: HttpClient) -> None:
        response = create_client_for_class.get('v1/breweries/random')
        response_from_check_func = check_response_random_brewery(get_list_breweries_response_model.validate_python(response))
        assert response_from_check_func[0], response_from_check_func[1]


