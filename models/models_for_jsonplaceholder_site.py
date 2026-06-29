from pydantic import BaseModel, EmailStr, TypeAdapter, Field
from typing import List, Annotated
import random
from faker import Faker

fake = Faker('en_US')

class PostModel(BaseModel):
    userId: int
    id: int
    title: str
    body: str

class PostCreateModel(BaseModel):
    userId: int = Field(default_factory=lambda: random.randint(1, 100))
    title: str = Field(default_factory=lambda: " ".join(fake.words(nb=random.randint(1, 10))))
    body: str = Field(default_factory=lambda: " ".join(fake.words(nb=random.randint(1, 10))))


class CommentModel(BaseModel):
    postId: int
    id: int
    name: str
    email: EmailStr
    body: str

class CommentUpdateModel(BaseModel):
    postId: int = Field(default_factory=lambda: random.randint(1, 100))
    id: int = Field(default_factory=lambda: random.randint(1, 100))
    name: str = Field(default_factory=lambda: " ".join(fake.words(nb=random.randint(1, 10))))
    email: EmailStr = Field(default_factory=lambda: fake.email())
    body: str = Field(default_factory=lambda: " ".join(fake.words(nb=random.randint(1, 10))))

class AlbumModel(BaseModel):
    userId: int | None = None
    id: int
    title: str

class AlbumUpdateModel(BaseModel):
    userId: int = Field(default_factory=lambda: random.randint(1, 100))
    id: int = Field(default_factory=lambda: random.randint(1, 100))
    title: str = Field(default_factory=lambda: " ".join(fake.words(nb=random.randint(1, 10))))

class PhotoModel(BaseModel):
    albumId: int
    id: int
    title: str
    url: str
    thumbnailUrl: str

class TodoModel(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool


class GeoModel(BaseModel):
    lat: float
    lng: float

class AddressModel(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: GeoModel

class CompanyModel(BaseModel):
    name: str
    catchPhrase: str
    bs: str

class UserModel(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    address: AddressModel
    phone: str
    website: str
    company: CompanyModel

get_list_posts_response_model = TypeAdapter(Annotated[List[PostModel], Field(min_length=1)])
get_list_comments_response_model = TypeAdapter(Annotated[List[CommentModel], Field(min_length=1)])
get_list_albums_response_model = TypeAdapter(Annotated[List[AlbumModel], Field(min_length=1)])
get_list_photos_response_model = TypeAdapter(Annotated[List[PhotoModel], Field(min_length=1)])
get_list_todos_response_model = TypeAdapter(Annotated[List[TodoModel], Field(min_length=1)])
get_list_users_response_model = TypeAdapter(Annotated[List[UserModel], Field(min_length=1)])

