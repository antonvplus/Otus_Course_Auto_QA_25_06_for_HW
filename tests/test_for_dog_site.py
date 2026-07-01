import pytest
from http_client import HttpClient
from models.models_for_dog_site import (GetListAllBreedsResponseModel,
                                        GetRandomImageResponseModel,
                                        GetMultipleImagesResponseModel,
                                        GetListSubBreedsResponseModel)
from service.services_for_dog_site import (check_response_list_all_breeds, check_response_random_image,
                                           check_response_random_multiple_image, check_response_list_all_sub_breeds)


@pytest.mark.parametrize('create_client_for_class', ['https://dog.ceo'], indirect=True)
class TestDogSite:

    @pytest.mark.dog
    def test_check_get_list_all_breeds(self, create_client_for_class: HttpClient) -> None:
        response = create_client_for_class.get('api/breeds/list/all')
        response_from_check_func = check_response_list_all_breeds(GetListAllBreedsResponseModel(**response))
        assert response_from_check_func[0], response_from_check_func[1]

    @pytest.mark.dog
    def test_check_get_random_image_from_all_dogs_collections(self, create_client_for_class: HttpClient) -> None:
        response = create_client_for_class.get('api/breeds/image/random')
        response_from_check_func = check_response_random_image(GetRandomImageResponseModel(**response))
        assert response_from_check_func[0], response_from_check_func[1]

    @pytest.mark.dog
    @pytest.mark.parametrize("breed", ["basenji", "chow", "dingo", "mix", "segugio"])
    def test_check_get_random_image_from_breed_collections(self, create_client_for_class: HttpClient, breed: str) -> None:
        response = create_client_for_class.get(f'api/breed/{breed}/images/random')
        response_model = GetRandomImageResponseModel(**response)
        assert breed in response_model.message, "There is no correct breed in the answer"
        response_from_check_func = check_response_random_image(GetRandomImageResponseModel(**response))
        assert response_from_check_func[0], response_from_check_func[1]

    @pytest.mark.dog
    @pytest.mark.parametrize("quantity", [1, 2, 3, 4, 5])
    def test_check_get_multiple_images_from_breed_collections(self, create_client_for_class: HttpClient, quantity: int) -> None:
        response = create_client_for_class.get(f'api/breed/hound/images/random/{quantity}')
        response_model = GetMultipleImagesResponseModel(**response)
        assert len(response_model.message) == quantity, "Incorrect number of images in the answer"
        response_from_check_func = check_response_random_multiple_image(GetMultipleImagesResponseModel(**response))
        assert response_from_check_func[0], response_from_check_func[1]

    @pytest.mark.dog
    @pytest.mark.parametrize("breed", ["australian", "bullterrier", "hound", "mastiff", "rajapalayam"])
    def test_check_get_list_all_sub_breeds(self, create_client_for_class: HttpClient, breed: str) -> None:
        response = create_client_for_class.get(f'api/breed/{breed}/list')
        response_from_check_func = check_response_list_all_sub_breeds(GetListSubBreedsResponseModel(**response))
        assert response_from_check_func[0], response_from_check_func[1]


