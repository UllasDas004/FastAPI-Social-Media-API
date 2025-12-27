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

@pytest.mark.parametrize("title, content, published, status_code",[
    ("1st title","1st content",True,201),
    ("2nd title","2nd content",True,201),
    ("3rd title","3rd content",False,201),
    (None,'Content',True,422),
    ('title',None,False,422)
])
def test_create_post(authorized_client,test_user,test_posts,title,content,published,status_code):
    response = authorized_client.post(
        "/posts/",json={'title' : title,'content' : content,'published' : published})
    assert response.status_code == status_code
    if response.status_code == 201:
        created_post = schemas.PostResponse(**response.json())
        assert created_post.title == title
        assert created_post.content == content
        assert created_post.published == published
        assert created_post.owner.id == test_user['id']

def test_create_post_default_published_true(authorized_client,test_posts,test_user):
    response = authorized_client.post(
        "/posts/",json={'title' : 'title','content' : 'content'})
    created_post = schemas.PostResponse(**response.json())
    assert response.status_code == 201
    assert created_post.title == 'title'
    assert created_post.content == 'content'
    assert created_post.published == True
    assert created_post.owner.id == test_user['id']

def test_unauthorized_user_create_post(client,test_posts):
    response = client.post("/posts/",json={'title' : 'title','content' : 'content'})
    assert response.status_code == 401


def test_unauthorized_user_delete_post(client,test_posts):
    response = client.delete(f"/posts/{test_posts[0].id}")
    assert response.status_code == 401

def test_delete_post_success(authorized_client,test_posts,test_user):
    response = authorized_client.delete(f"/posts/{test_posts[0].id}")
    assert response.status_code == 204

def test_delete_post_non_exist(authorized_client,test_posts,test_user):
    response = authorized_client.delete("/posts/100")
    assert response.status_code == 404

def test_delete_other_user_post(authorized_client,test_posts,test_user):
    response = authorized_client.delete(f"/posts/{test_posts[3].id}")
    assert response.status_code == 403

def test_update_post(authorized_client,test_posts,test_user):
    data = {
        'title' : 'updated title',
        'content' : 'updated content',
        'id' : test_posts[0].id
    }
    response = authorized_client.put(f"/posts/{test_posts[0].id}",json = data)
    updated_post = schemas.PostResponse(**response.json())
    assert response.status_code == 200
    assert updated_post.title == 'updated title'
    assert updated_post.content == 'updated content'
    assert updated_post.id == test_posts[0].id

def test_update_other_user_post(authorized_client,test_posts,test_user):
    data = {
        'title' : 'updated title',
        'content' : 'updated content',
        'id' : test_posts[3].id
    }
    response = authorized_client.put(f"/posts/{test_posts[3].id}",json = data)
    assert response.status_code == 403

def test_unauthorized_user_update_post(client,test_posts):
    response = client.put(f"/posts/{test_posts[0].id}")
    assert response.status_code == 401

def test_update_post_non_exist(authorized_client,test_posts,test_user):
    data = {
        'title' : 'updated title',
        'content' : 'updated content',
        'id' : 100
    }
    response = authorized_client.put("/posts/100",json = data)
    assert response.status_code == 404
