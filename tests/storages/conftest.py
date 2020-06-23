from freezegun import freeze_time
import pytest

from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.storages.dtos import (
    UserDto,
    ReactionDto,
    CommentDto,
    PostDto
)
from fb_post_v2.models import User, Post, Comment, Reaction

@pytest.fixture
def users():
    user_dict = [
    	{
    	    "name": "anusha",
    	    "username": "anu-nandu"
    	    
    	},
        {
            "name": "Sneha",
            "username": "sneha-mallampalli"
        },
        {
            "name": "Suma",
            "username": "suma-pulla"
        },
    ]
    user_dict_list = []
    for user in user_dict:
        user_dict_list.append(User(**user))
    User.objects.bulk_create(user_dict_list)

@pytest.fixture
@freeze_time('2020-04-17 00:00:00+00:00')
def posts(users):
    post_dict = [
        {
            "content": "Hello ALL",
            "posted_by_id": 1
        },
        {
            "content": "Good Morning",
            "posted_by_id": 1
        },
        {
            "content": "Hello Everyone",
            "posted_by_id": 2
        },
    ]
    post_dict_list = []
    for post in post_dict:
        post_dict_list.append(Post(**post))
    Post.objects.bulk_create(post_dict_list)

@pytest.fixture
@freeze_time('2020-04-17 00:00:00+00:00')
def comments(posts):
    comments_dict_list = []
    comments_dict = [
        {
            "content" : "Hii",
            "commented_by_id" : 2,
            "post_id" : 1,
            "parent_comment_id" : None,
        },
        {
            "content" : "Hello",
            "commented_by_id" : 1,
            "post_id" : 1,
            "parent_comment_id" : 1,
        },
    ]
    for comment in comments_dict:
        comments_dict_list.append(Comment(**comment))
    Comment.objects.bulk_create(comments_dict_list)

@pytest.fixture
@freeze_time('2020-04-17 00:00:00+00:00')
def reactions(comments):
    reactions_dict_list = []
    reactions_dict = [
        {
            "post_id" : 2,
            "comment_id" : None,
            "reaction" : "LIT",
            "reacted_by_id" : 2
        },
        {
            "post_id" : None,
            "comment_id" : 1,
            "reaction" : "THUMBS-UP",
            "reacted_by_id" : 2,
        },
    ]
    for react in reactions_dict:
        reactions_dict_list.append(Reaction(**react))
    Reaction.objects.bulk_create(reactions_dict_list)
