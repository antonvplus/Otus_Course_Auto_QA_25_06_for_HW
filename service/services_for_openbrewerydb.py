from models.models_for_openbrewerydb_site import GetSingleBreweryResponseModel
from typing import List, Tuple

first_brewery = {
        "id": "ae7b3174-8be8-4d53-a3a5-9b8240970eea",
        "name": "'s",
        "brewery_type": "brewpub",
        "address_1": "1 Friesener Straße",
        "address_2": None,
        "address_3": None,
        "city": "Kronach",
        "state_province": "Bayern",
        "postal_code": "96317",
        "country": "Germany",
        "longitude": 11.327765,
        "latitude": 50.241246,
        "phone": "+49 9261 628000",
        "website_url": "http://www.antla.de",
        "state": "Bayern",
        "street": "1 Friesener Straße"
    }

breweries_for_test_id = {"ee6d39c6-092f-4623-8099-5b8643f70dbe": {'id': 'ee6d39c6-092f-4623-8099-5b8643f70dbe', 'name': '16 Stone Brewpub', 'brewery_type': 'brewpub', 'address_1': '9542 Main St', 'address_2': None, 'address_3': None, 'city': 'Holland Patent', 'state_province': 'New York', 'postal_code': '13354', 'country': 'United States', 'longitude': -75.2565195, 'latitude': 43.24211175, 'phone': '3158658500', 'website_url': 'http://www.16stonebrewpub.com', 'state': 'New York', 'street': '9542 Main St'},
                         "6c53984f-fac1-4ea7-9c44-44e25897c71a": {'id': '6c53984f-fac1-4ea7-9c44-44e25897c71a', 'name': '14th Star Brewing', 'brewery_type': 'micro', 'address_1': '133 N Main St Ste 7', 'address_2': None, 'address_3': None, 'city': 'Saint Albans', 'state_province': 'Vermont', 'postal_code': '05478-1735', 'country': 'United States', 'longitude': None, 'latitude': None, 'phone': '8025285988', 'website_url': 'http://www.14thstarbrewing.com', 'state': 'Vermont', 'street': '133 N Main St Ste 7'},
                         "45119c56-345b-4adc-b481-c5cf7bfe98c4": {'id': '45119c56-345b-4adc-b481-c5cf7bfe98c4', 'name': '13 Stripes Brewery', 'brewery_type': 'brewpub', 'address_1': '250 Mill St, Suite PW3101', 'address_2': None, 'address_3': None, 'city': 'Taylors', 'state_province': 'South Carolina', 'postal_code': '29687', 'country': 'United States', 'longitude': None, 'latitude': None, 'phone': '8643491430', 'website_url': 'http://www.13StripesBrewery.com', 'state': 'South Carolina', 'street': '250 Mill St, Suite PW3101'},
                         "08f78223-24f8-4b71-b381-ea19a5bd82df": {'id': '08f78223-24f8-4b71-b381-ea19a5bd82df', 'name': '11 Below Brewing Company', 'brewery_type': 'micro', 'address_1': '6820 Bourgeois Rd', 'address_2': None, 'address_3': None, 'city': 'Houston', 'state_province': 'Texas', 'postal_code': '77066-3107', 'country': 'United States', 'longitude': -95.5186591, 'latitude': 29.9515464, 'phone': '2814442337', 'website_url': 'http://www.11belowbrewing.com', 'state': 'Texas', 'street': '6820 Bourgeois Rd'},
                         "ae7b3174-8be8-4d53-a3a5-9b8240970eea": {'id': 'ae7b3174-8be8-4d53-a3a5-9b8240970eea', 'name': "'s", 'brewery_type': 'brewpub', 'address_1': '1 Friesener Straße', 'address_2': None, 'address_3': None, 'city': 'Kronach', 'state_province': 'Bayern', 'postal_code': '96317', 'country': 'Germany', 'longitude': 11.327765, 'latitude': 50.241246, 'phone': '+49 9261 628000', 'website_url': 'http://www.antla.de', 'state': 'Bayern', 'street': '1 Friesener Straße'}}

def check_response_list_all_breweries(response_model: List[GetSingleBreweryResponseModel] ) -> Tuple[bool, str|None]:
    if not isinstance(response_model, list):
        return False, f"Unexpected response type: {type(response_model)}"
    if len(response_model) == 0:
        return False, "Empty list of all breweries"
    if response_model[0] != GetSingleBreweryResponseModel(**first_brewery):
        return False, "The response does not match the expected structure"
    return True, None

def check_response_list_found_breweries(response_model: List[GetSingleBreweryResponseModel] ) -> Tuple[bool, str|None]:
    if not isinstance(response_model, list):
        return False, f"Unexpected response type: {type(response_model)}"
    if len(response_model) == 0:
        return False, "Empty list of all breweries"
    return True, None

def check_response_single_brewery(response_model: GetSingleBreweryResponseModel, term: str) -> Tuple[bool, str|None]:
    if response_model != GetSingleBreweryResponseModel(**breweries_for_test_id[term]):
        return False, "The response does not match the expected structure"
    return True, None

def check_response_random_brewery(response_model: List[GetSingleBreweryResponseModel] ) -> Tuple[bool, str|None]:
    if not isinstance(response_model, list):
        return False, f"Unexpected response type: {type(response_model)}"
    if len(response_model) != 1:
        return False, "Empty list of all breweries"
    return True, None