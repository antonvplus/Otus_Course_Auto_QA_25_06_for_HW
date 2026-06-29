from pydantic import BaseModel, TypeAdapter, Field
from typing import List, Annotated

class GetSingleBreweryResponseModel(BaseModel):
    id: str
    name: str
    brewery_type: str
    address_1: str | None
    address_2: str | None
    address_3: str | None
    city: str
    state_province: str
    postal_code: str | None
    country: str
    longitude: float| None
    latitude: float| None
    phone: str | None
    website_url: str | None
    state: str
    street: str | None

get_list_breweries_response_model = TypeAdapter(Annotated[List[GetSingleBreweryResponseModel], Field(min_length=1)])
