import pytest
from http_client import HttpClient
from models.models_for_jsonplaceholder_site import (get_list_albums_response_model, get_list_photos_response_model,
                                                    get_list_posts_response_model, get_list_todos_response_model,
                                                    get_list_users_response_model, get_list_comments_response_model,
                                                    PostCreateModel, PostModel,
                                                    CommentUpdateModel, CommentModel,
                                                    AlbumUpdateModel, AlbumModel)

site = "jsonplaceholder"
client = HttpClient(site)

@pytest.mark.jsonplaceholder
@pytest.mark.parametrize("resource",
                         [pytest.param('posts', id='posts'),
                          pytest.param('comments', id = 'comments'),
                          pytest.param('albums', id='albums'),
                          pytest.param('photos', id='photos'),
                          pytest.param('todos', id='todos'),
                          pytest.param('users', id='users')])
def test_check_get_list_all_resources(resource: str) -> None:
    response = client.get(resource)
    if resource == 'posts':
        get_list_posts_response_model.validate_python(response)
    elif resource == 'comments':
        get_list_comments_response_model.validate_python(response)
    elif resource == 'albums':
        get_list_albums_response_model.validate_python(response)
    elif resource == 'photos':
        get_list_photos_response_model.validate_python(response)
    elif resource == 'todos':
        get_list_todos_response_model.validate_python(response)
    elif resource == 'users':
        get_list_users_response_model.validate_python(response)

@pytest.mark.jsonplaceholder
def test_check_create_resource() -> None:
    body = PostCreateModel().model_dump()
    response = client.post('posts', body=body)
    response_model = PostModel(**response)
    assert (response_model.userId == body['userId'] and
            response_model.title == body['title'] and
            response_model.body == body['body']), "The created object does not match"

@pytest.mark.jsonplaceholder
def test_check_update_resource() -> None:
    body = CommentUpdateModel().model_dump()
    response = client.put(f'comments/{body['id']}', body=body)
    response_model = CommentModel(**response)
    assert CommentModel(**body) == response_model, "The updated object does not match"

@pytest.mark.jsonplaceholder
def test_check_patch_resource() -> None:
    body = AlbumUpdateModel().model_dump()
    response = client.put(f'comments/{body['id']}', body={'title' :body['title']})
    AlbumModel(**response)
    assert response['title'] == body['title'], "The value has not been updated."

@pytest.mark.jsonplaceholder
@pytest.mark.parametrize("resource, id",
                         [pytest.param('posts', 1, id='posts'),
                          pytest.param('comments', 2, id = 'comments'),
                          pytest.param('albums', 3, id='albums'),
                          pytest.param('photos', 4, id='photos'),
                          pytest.param('todos', 5, id='todos'),
                          pytest.param('users', 6, id='users')])
def test_check_delete_resources(resource: str, id: int) -> None:
    client.delete(f'{resource}/{id}')
