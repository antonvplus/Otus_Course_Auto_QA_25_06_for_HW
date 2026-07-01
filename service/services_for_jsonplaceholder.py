from typing import Tuple

def check_response_list_all_recourses(response_model) -> Tuple[bool, str|None]:
    if not isinstance(response_model, list):
        return False, f"Unexpected response type: {type(response_model)}"
    if len(response_model) == 0:
        return False, "Empty list of all recourses"
    return True, None

