from typing import List
from app import schemas
import pytest

def test_get_all_posts(client,test_posts):
    response = client.get("/posts/")
    def validate(post):
        return schemas.PostOut(**post)
    post_map = map(validate,response.json())

    assert len(response.json()) == len(test_posts)
    assert response.status_code == 200

@pytest.mark.parametrize("id, status_code",[
    (1,200),
    (5,404),
    (None,422)
])
def test_get_one_post(client,test_posts,id,status_code):
    response = client.get(f"/posts/{id}")
    if response.status_code == 200:
        post = schemas.PostOut(**response.json())
        print(post)
        assert post.Post.id == id
    assert response.status_code == status_code