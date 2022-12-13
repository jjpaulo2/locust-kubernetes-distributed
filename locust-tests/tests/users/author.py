from random import randint

from locust import HttpUser, task, tag
from locust.clients import Response

from tests.schemas.author import new_author, new_author_name
from tests.settings import Auth


class AuthorHttpUser(HttpUser):
    next_to_update = 1

    def _set_next_to_update(self, response: Response) -> None:
        response_json = response.json().get('results')
        author_to_delete = randint(0, len(response_json) - 1)
        self.next_to_update = response_json[author_to_delete].get('pk')

    @tag('author', 'get')
    @task(5)
    def get_authors(self) -> None:
        response = self.client.get(
            '/authors/',
            name='get_authors'
        )
        self._set_next_to_update(response)

    @tag('author', 'post')
    @task(3)
    def create_author(self) -> None:
        self.client.post(
            '/authors/',
            name='create_author',
            json=new_author(),
            auth=Auth.basic(),
        )

    @tag('author', 'delete')
    @task(1)
    def delete_author(self) -> None:
        self.client.delete(
            f'/authors/{self.next_to_update}/',
            name='delete_author',
            auth=Auth.basic()
        )

    @tag('author', 'patch')
    @task(1)
    def update_author_name(self) -> None:
        self.client.patch(
            f'/authors/{self.next_to_update}/',
            name='update_author_name',
            json=new_author_name(),
            auth=Auth.basic()
        )

    @tag('author', 'put')
    @task(1)
    def update_author_data(self) -> None:
        self.client.put(
            f'/authors/{self.next_to_update}/',
            name='update_author_data',
            json=new_author(),
            auth=Auth.basic()
        )
