from pydantic import BaseModel, Field, field_validator
from typing import Literal

class GetListAllBreedsResponseModel(BaseModel):
    message: dict[str, list] = Field(min_length=1)
    status: Literal["success"]

class GetRandomImageResponseModel(BaseModel):
    message: str
    status: Literal["success"]

    @field_validator("message")
    @classmethod
    def check_image_response(cls, line: str) -> str:
        if ".jpg" not in line:
            raise ValueError("There is no image in the answer")
        return line


class GetMultipleImagesResponseModel(BaseModel):
    message: list[str]
    status: Literal["success"]

    @field_validator("message")
    @classmethod
    def check_images_response(cls, lines: str) -> str:
        if all('.jpg' in e for e in lines):
            return lines
        else:
            raise ValueError("There is no image in the answer")

class GetListSubBreedsResponseModel(BaseModel):
    message: list[str]
    status: Literal["success"]
