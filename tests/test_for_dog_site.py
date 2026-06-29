import pytest
from http_client import HttpClient
from models.models_for_dog_site import (GetListAllBreedsResponseModel,
                                        GetRandomImageResponseModel,
                                        GetMultipleImagesResponseModel,
                                        GetListSubBreedsResponseModel)

site = "dog"
client = HttpClient(site)

@pytest.mark.dog
def test_check_get_list_all_breeds() -> None:
    response = client.get('api/breeds/list/all')
    GetListAllBreedsResponseModel(**response)

@pytest.mark.dog
def test_check_get_random_image_from_all_dogs_collections() -> None:
    response = client.get('api/breeds/image/random')
    GetRandomImageResponseModel(**response)

@pytest.mark.dog
@pytest.mark.parametrize("breed", ["basenji", "chow", "dingo", "mix", "segugio"])
def test_check_get_random_image_from_breed_collections(breed: str) -> None:
    response = client.get(f'api/breed/{breed}/images/random')
    response_model = GetRandomImageResponseModel(**response)
    assert breed in response_model.message, "There is no correct breed in the answer"

@pytest.mark.dog
@pytest.mark.parametrize("quantity", [1, 2, 3, 4, 5])
def test_check_get_multiple_images_from_breed_collections(quantity: int) -> None:
    response = client.get(f'api/breed/hound/images/random/{quantity}')
    response_model = GetMultipleImagesResponseModel(**response)
    assert len(response_model.message) == quantity, "Incorrect number of images in the answer"

@pytest.mark.dog
@pytest.mark.parametrize("breed", ["airedale", "bullterrier", "hound", "mastiff", "rajapalayam"])
def test_check_get_list_all_sub_breeds(breed: str) -> None:
    response = client.get(f'api/breed/{breed}/list')
    GetListSubBreedsResponseModel(**response)

