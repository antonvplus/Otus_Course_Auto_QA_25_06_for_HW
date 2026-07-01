from models.models_for_dog_site import (GetListAllBreedsResponseModel, GetRandomImageResponseModel,
                                        GetMultipleImagesResponseModel, GetListSubBreedsResponseModel)


def check_response_list_all_breeds(response_model: GetListAllBreedsResponseModel) -> tuple[bool, str|None]:
    if not isinstance(response_model.message, dict):
        return False, f"Unexpected response type in message field: {type(response_model.message)}"
    if len(response_model.message) == 0:
        return False, "Empty list of all dog breeds"
    if response_model.status != 'success':
        return False, f"Invalid response status: {response_model.status}"
    return True, None

def check_response_random_image(response_model: GetRandomImageResponseModel) -> tuple[bool, str|None]:
    if not isinstance(response_model.message, str):
        return False, f"Unexpected response type in message field: {type(response_model.message)}"
    if ".jpg" not in response_model.message:
        return False, "There is no image in the answer"
    if response_model.status != 'success':
        return False, f"Invalid response status: {response_model.status}"
    return True, None

def check_response_random_multiple_image(response_model: GetMultipleImagesResponseModel) -> tuple[bool, str|None]:
    if not isinstance(response_model.message, list):
        return False, f"Unexpected response type in message field: {type(response_model.message)}"
    if any(".jpg" not in line for line in response_model.message):
        return False, "There is no image in the answer"
    if response_model.status != 'success':
        return False, f"Invalid response status: {response_model.status}"
    return True, None

def check_response_list_all_sub_breeds(response_model: GetListSubBreedsResponseModel) -> tuple[bool, str|None]:
    if not isinstance(response_model.message, list):
        return False, f"Unexpected response type in message field: {type(response_model.message)}"
    if len(response_model.message) == 0:
        return False, "Empty list of all dog sub-breeds"
    if response_model.status != 'success':
        return False, f"Invalid response status: {response_model.status}"
    return True, None