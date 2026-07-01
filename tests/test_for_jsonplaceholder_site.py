import pytest
from http_client import HttpClient
from models.models_for_jsonplaceholder_site import (get_list_albums_response_model, get_list_photos_response_model,
                                                    get_list_posts_response_model, get_list_todos_response_model,
                                                    get_list_users_response_model, get_list_comments_response_model,
                                                    PostCreateModel, PostModel,
                                                    CommentUpdateModel, CommentModel,
                                                    AlbumUpdateModel, AlbumModel)
from service.services_for_jsonplaceholder import check_response_list_all_recourses

@pytest.mark.parametrize('create_client_for_class', ['https://jsonplaceholder.typicode.com'], indirect=True)
class TestJsonPlaceholderSite:
    @pytest.mark.jsonplaceholder
    @pytest.mark.parametrize("resource",
                             [pytest.param('posts', id='posts'),
                              pytest.param('comments', id='comments'),
                              pytest.param('albums', id='albums'),
                              pytest.param('photos', id='photos'),
                              pytest.param('todos', id='todos'),
                              pytest.param('users', id='users')])
    def test_check_get_list_all_resources(self, create_client_for_class: HttpClient, resource: str) -> None:
        response = create_client_for_class.get(resource)
        if resource == 'posts':
            response_model = get_list_posts_response_model.validate_python(response)
        elif resource == 'comments':
            response_model = get_list_comments_response_model.validate_python(response)
        elif resource == 'albums':
            response_model = get_list_albums_response_model.validate_python(response)
        elif resource == 'photos':
            response_model = get_list_photos_response_model.validate_python(response)
        elif resource == 'todos':
            response_model = get_list_todos_response_model.validate_python(response)
        elif resource == 'users':
            response_model = get_list_users_response_model.validate_python(response)
        response_from_check_func =check_response_list_all_recourses(response_model)
        assert response_from_check_func[0], response_from_check_func[1]

    @pytest.mark.jsonplaceholder
    def test_check_create_resource(self, create_client_for_class: HttpClient) -> None:
        body = PostCreateModel().model_dump()
        response = create_client_for_class.post('posts', body=body)
        response_model = PostModel(**response)
        assert (response_model.userId == body['userId'] and
                response_model.title == body['title'] and
                response_model.body == body['body']), "The created object does not match"

    @pytest.mark.jsonplaceholder
    def test_check_update_resource(self, create_client_for_class: HttpClient) -> None:
        body = CommentUpdateModel().model_dump()
        response = create_client_for_class.put(f"comments/{body['id']}", body=body)
        response_model = CommentModel(**response)
        assert CommentModel(**body) == response_model, "The updated object does not match"

    @pytest.mark.jsonplaceholder
    def test_check_patch_resource(self, create_client_for_class: HttpClient) -> None:
        body = AlbumUpdateModel().model_dump()
        response = create_client_for_class.patch(f"albums/{body['id']}", body={'title': body['title']})
        response_model = AlbumModel.model_validate(response)
        assert response_model.title == body['title'], "The value has not been updated."

    @pytest.mark.jsonplaceholder
    @pytest.mark.parametrize("resource, id",
                             [pytest.param('posts', 1, id='posts'),
                              pytest.param('comments', 2, id='comments'),
                              pytest.param('albums', 3, id='albums'),
                              pytest.param('photos', 4, id='photos'),
                              pytest.param('todos', 5, id='todos'),
                              pytest.param('users', 6, id='users')])
    def test_check_delete_resources(self, create_client_for_class: HttpClient, resource: str, id: int) -> None:
        create_client_for_class.delete(f'{resource}/{id}', code=200)

