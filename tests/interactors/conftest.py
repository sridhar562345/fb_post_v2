import datetime

import pytest

from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.storages.dtos import (
    UserDto,
    ReactionDto,
    CommentDto,
    PostDto,
    PostReactionsDto,
    PostCommentCountDto,
    CommentReactionMetricsDto,
    CommentRepliesCountDto
)

@pytest.fixture()
def user_dtos():
    user_dtos = [
        UserDto(
            id=1,
            name="Anusha",
            profile_pic="avatar.png",
        ),
        UserDto(
            id=2,
            name="Sneha",
            profile_pic="avatar.png",
        ),
    ]
    return user_dtos

@pytest.fixture()
def post_dto():
    post_dto = \
        PostDto(
            id=1,
            posted_by_id=1,
            post_content="My first post",
            posted_at=datetime.datetime(2020, 5, 20, 0, 0),
        ),
    return post_dto

@pytest.fixture()
def post():
    post_dto = \
        PostDto(
            id=2,
            posted_by_id=1,
            post_content="My second post",
            posted_at=datetime.datetime(2020, 5, 20, 0, 0),
        ),
    return post_dto



@pytest.fixture()
def post_dtos():
    post_dtos = [
        PostDto(
            id=1,
            posted_by_id=1,
            post_content="My first post",
            posted_at=datetime.datetime(2020, 5, 20, 0, 0),
        ),
        PostDto(
            id=2,
            posted_by_id=1,
            post_content="My second post",
            posted_at=datetime.datetime(2020, 5, 20, 0, 0),
        )
    ]
    return post_dtos

@pytest.fixture()
def comment_dtos():
    comment_dtos = [
        CommentDto(
            id=1,
            commented_by_id=2,
            post_id=1,
            comment_content="nice post",
            commented_at=datetime.datetime(2020, 5, 20, 0, 0),
            parent_comment_id=None
        ),
        CommentDto(
            id=2,
            commented_by_id=1,
            post_id=1,
            comment_content="reply to comment",
            commented_at=datetime.datetime(2020, 5, 20, 0, 0),
            parent_comment_id=1
        ),
        CommentDto(
            id=3,
            commented_by_id=2,
            post_id=1,
            comment_content="reply to reply",
            commented_at=datetime.datetime(2020, 5, 20, 0, 0),
            parent_comment_id=1
        )
    ]
    return comment_dtos

@pytest.fixture()
def reply_dtos():
    reply_dtos = [
        CommentDto(
            id=2,
            commented_by_id=1,
            post_id=1,
            comment_content="reply to comment",
            commented_at=datetime.datetime(2020, 5, 20, 0, 0),
            parent_comment_id=1
        ),
        CommentDto(
            id=3,
            commented_by_id=2,
            post_id=1,
            comment_content="reply to reply",
            commented_at=datetime.datetime(2020, 5, 20, 0, 0),
            parent_comment_id=1
        )
    ]
    return reply_dtos


@pytest.fixture()
def reaction_dtos():
    reaction_dtos = [
        ReactionDto(
            id=1,
            post_id=1,
            reacted_by_id=1,
            reaction=ReactionType.LIKE.value,
            comment_id=None
        ),
        ReactionDto(
            id=2,
            post_id=None,
            reacted_by_id=1,
            reaction=ReactionType.SAD.value,
            comment_id=1
        ),
        ReactionDto(
            id=3,
            comment_id=None,
            post_id=1,
            reacted_by_id=2,
            reaction=ReactionType.HAHA.value
        ),
    ]
    return reaction_dtos

@pytest.fixture()
def post_reactions_dtos():
    post_reactions_dtos = [
        ReactionDto(
            id=1,
            post_id=1,
            reacted_by_id=1,
            reaction=ReactionType.LIKE.value,
            comment_id=None
        ),
        ReactionDto(
            id=3,
            comment_id=None,
            post_id=1,
            reacted_by_id=2,
            reaction=ReactionType.HAHA.value
        ),
    ]
    return post_reactions_dtos

@pytest.fixture()
def post_reactions_dto():
    post_reactions_dto = PostReactionsDto(
        post_id=1,
        reactions_count = 2,
        reactions_list = ["LIKE", "HAHA"],
    )
    return post_reactions_dto

@pytest.fixture()
def post_comments_count_dto():
    post_comments_count_dto = PostCommentCountDto(
        post_id=1,
        comments_count = 1
    )
    return post_comments_count_dto


@pytest.fixture()
def user_post_fields_single_post_dtos():
    post_fields = {}
    post_dtos = [
        PostDto(
            id=2,
            posted_by_id=1,
            post_content="My second post",
            posted_at=datetime.datetime(2020, 5, 20, 0, 0),
        ),
    ]
    post_reactions_dtos = [
        PostReactionsDto(
            post_id=2,
            reactions_count = 0,
            reactions_list = [],
        )
    ]
    post_comments_count_dtos = [
        PostCommentCountDto(
            post_id=2,
            comments_count = 1
        )
    ]
    post_fields["post_dto"] = post_dtos
    post_fields["post_reactions_dtos"] = post_reactions_dtos
    post_fields["post_comments_count_dtos"] = post_comments_count_dtos
    
    return post_fields


@pytest.fixture()
def user_post_fields_double_posts_dtos():
    post_fields = {}
    post_dtos = [
        PostDto(
            id=2,
            posted_by_id=1,
            post_content="My second post",
            posted_at=datetime.datetime(2020, 5, 20, 0, 0),
        ),
        PostDto(
            id=1,
            posted_by_id=1,
            post_content="My first post",
            posted_at=datetime.datetime(2020, 5, 20, 0, 0),
        ),
    ]
    post_reactions_dtos = [
        PostReactionsDto(
            post_id=2,
            reactions_count = 0,
            reactions_list = [],
        ),
        PostReactionsDto(
            post_id=1,
            reactions_count = 0,
            reactions_list = [],
        )
    ]
    post_comments_count_dtos = [
        PostCommentCountDto(
            post_id=2,
            comments_count = 0
        ),
        PostCommentCountDto(
            post_id=1,
            comments_count = 1
        )
    ]
    post_fields["post_dto"] = post_dtos
    post_fields["post_reactions_dtos"] = post_reactions_dtos
    post_fields["post_comments_count_dtos"] = post_comments_count_dtos
    
    return post_fields

    
@pytest.fixture()
def user_post_two_posts_dtos():
    all_fields = {}
    comment_dtos = [
        CommentDto(
            id=1,
            commented_by_id=2,
            post_id=1,
            comment_content="nice post",
            commented_at=datetime.datetime(2020, 5, 20, 0, 0),
            parent_comment_id=None
        ),
    ]
    comment_reaction_metrics_dto = [
        CommentReactionMetricsDto(
            comment_id = 1,
            reactions_count = 0,
            reactions_list =  []
        )
    ]
    comment_replies_count_dtos = [
        CommentRepliesCountDto(
            comment_id = 1,
            replies_count = 0
        )
    ]
    reaction_dtos = []
    user_dtos = [
        UserDto(
            id=1,
            name="Anusha",
            profile_pic="avatar.png",
        ),
    ]
    all_fields = {
        "user_dtos": user_dtos,
        "comment_dtos": comment_dtos,
        "reaction_dtos": reaction_dtos,
        "comment_reaction_metrics_dto": comment_reaction_metrics_dto,
        "comment_replies_count_dtos": comment_replies_count_dtos
    }
    return all_fields


@pytest.fixture()
def no_comments_post_dtos():
    all_fields = {}
    post_reactions_dto = PostReactionsDto(
        post_id=2,
        reactions_count = 0,
        reactions_list = [],
    )
    post_comments_count_dto = PostCommentCountDto(
        post_id=2,
        comments_count = 0
    )
    comment_dtos = []
    comment_reaction_metrics_dto = []
    comment_replies_count_dtos = []
    reaction_dtos = []
    user_dtos = [
        UserDto(
            id=1,
            name="Anusha",
            profile_pic="avatar.png",
        ),
    ]
    post_dto = \
        PostDto(
            id=2,
            posted_by_id=1,
            post_content="My second post",
            posted_at=datetime.datetime(2020, 5, 20, 0, 0),
        ),
    all_fields = {
        "post_dto": post_dto,
        "user_dtos": user_dtos,
        "comment_dtos": comment_dtos,
        "reaction_dtos": reaction_dtos,
        "post_reactions_dto": post_reactions_dto,
        "post_comments_count_dto":post_comments_count_dto,
        "comment_reaction_metrics_dto": comment_reaction_metrics_dto,
        "comment_replies_count_dtos": comment_replies_count_dtos
    }
    return all_fields

@pytest.fixture()
def no_comments_post_fields():
    post_fields = {}
    post_reactions_dtos = [
        PostReactionsDto(
            post_id=2,
            reactions_count = 0,
            reactions_list = [],
        )
    ]
    post_comments_count_dtos = [
        PostCommentCountDto(
            post_id=2,
            comments_count = 0
        )
    ]
    post_dtos = [
        PostDto(
            id=2,
            posted_by_id=1,
            post_content="My second post",
            posted_at=datetime.datetime(2020, 5, 20, 0, 0),
        ),
    ]
    post_fields["post_dto"] = post_dtos
    post_fields["post_reactions_dtos"] = post_reactions_dtos
    post_fields["post_comments_count_dtos"] = post_comments_count_dtos
    
    return post_fields
    

@pytest.fixture()
def multiple_repeated_reactions_for_post():
    all_fields = {}
    post_reactions_dto = PostReactionsDto(
        post_id=2,
        reactions_count = 3,
        reactions_list = ["WOW", "HAHA"],
    )
    post_comments_count_dto = PostCommentCountDto(
        post_id=2,
        comments_count=0
    )
    comment_dtos = []
    comment_reaction_metrics_dto = []
    comment_replies_count_dtos = []
    reaction_dtos = [
        ReactionDto(
            id=1,
            post_id=2,
            reacted_by_id=1,
            reaction=ReactionType.WOW.value,
            comment_id=None
        ),
        ReactionDto(
            id=2,
            post_id=2,
            reacted_by_id=2,
            reaction=ReactionType.WOW.value,
            comment_id=None
        ),
        ReactionDto(
            id=3,
            comment_id=None,
            post_id=2,
            reacted_by_id=3,
            reaction=ReactionType.HAHA.value
        ),
    ]
    user_dtos = [
        UserDto(
            id=1,
            name="Anusha",
            profile_pic="avatar.png",
        ),
        UserDto(
            id=2,
            name="Sneha",
            profile_pic="avatar.png",
        ),
        UserDto(
            id=3,
            name="Suma",
            profile_pic="avatar.png",
        ),
    ]
    post_dto = \
        PostDto(
            id=2,
            posted_by_id=1,
            post_content="My second post",
            posted_at=datetime.datetime(2020, 5, 20, 0, 0),
        ),
    all_fields = {
        "post_dto": post_dto,
        "user_dtos": user_dtos,
        "comment_dtos": comment_dtos,
        "reaction_dtos": reaction_dtos,
        "post_reactions_dto": post_reactions_dto,
        "post_comments_count_dto": post_comments_count_dto,
        "comment_reaction_metrics_dto": comment_reaction_metrics_dto,
        "comment_replies_count_dtos": comment_replies_count_dtos
    }
    return all_fields

@pytest.fixture()
def user_post_fields_single_post_multiple_reactions_dtos():
    post_fields = {}
    post_dtos = [
        PostDto(
            id=2,
            posted_by_id=1,
            post_content="My second post",
            posted_at=datetime.datetime(2020, 5, 20, 0, 0),
        ),
    ]
    post_reactions_dtos = [
        PostReactionsDto(
            post_id=2,
            reactions_count = 3,
            reactions_list = ["WOW", "HAHA"],
        )
    ]
    post_comments_count_dtos = [
        PostCommentCountDto(
            post_id=2,
            comments_count=0
        )
    ]
    post_fields["post_dto"] = post_dtos
    post_fields["post_reactions_dtos"] = post_reactions_dtos
    post_fields["post_comments_count_dtos"] = post_comments_count_dtos
    
    return post_fields


@pytest.fixture()
def no_comments_reply_post_dtos():
    all_fields = {}
    post_reactions_dto = PostReactionsDto(
        post_id=2,
        reactions_count = 0,
        reactions_list = [],
    )
    post_comments_count_dto = PostCommentCountDto(
        post_id=2,
        comments_count = 1
    )
    comment_dtos = [
        CommentDto(
            id=1,
            commented_by_id=2,
            post_id=2,
            comment_content="nice post",
            commented_at=datetime.datetime(2020, 5, 20, 0, 0),
            parent_comment_id=None
        ),
    ]
    comment_reaction_metrics_dto = [
        CommentReactionMetricsDto(
            comment_id = 1,
            reactions_count = 0,
            reactions_list =  []
        )
    ]
    comment_replies_count_dtos = [
        CommentRepliesCountDto(
            comment_id = 1,
            replies_count = 0
        )
    ]
    reaction_dtos = []
    user_dtos = [
        UserDto(
            id=1,
            name="Anusha",
            profile_pic="avatar.png",
        ),
    ]
    post_dto = \
        PostDto(
            id=2,
            posted_by_id=1,
            post_content="My second post",
            posted_at=datetime.datetime(2020, 5, 20, 0, 0),
        ),
    all_fields = {
        "post_dto": post_dto,
        "user_dtos": user_dtos,
        "comment_dtos": comment_dtos,
        "reaction_dtos": reaction_dtos,
        "post_reactions_dto": post_reactions_dto,
        "post_comments_count_dto": post_comments_count_dto,
        "comment_reaction_metrics_dto": comment_reaction_metrics_dto,
        "comment_replies_count_dtos": comment_replies_count_dtos
    }
    return all_fields

@pytest.fixture()
def single_comment_post_fields():
    post_fields = {}
    post_reactions_dtos = [
        PostReactionsDto(
            post_id=2,
            reactions_count = 0,
            reactions_list = [],
        )
    ]
    post_comments_count_dtos = [
        PostCommentCountDto(
            post_id=2,
            comments_count = 1
        )
    ]
    post_dtos = [
        PostDto(
            id=2,
            posted_by_id=1,
            post_content="My second post",
            posted_at=datetime.datetime(2020, 5, 20, 0, 0),
        ),
    ]
    post_fields["post_dto"] = post_dtos
    post_fields["post_reactions_dtos"] = post_reactions_dtos
    post_fields["post_comments_count_dtos"] = post_comments_count_dtos
    
    return post_fields


@pytest.fixture()
def post_with_one_comment_with_one_reply():
    all_fields = {}
    post_reactions_dto = PostReactionsDto(
        post_id=2,
        reactions_count = 0,
        reactions_list = [],
    )
    post_comments_count_dto = PostCommentCountDto(
        post_id=2,
        comments_count=1
    )
    comment_dtos = [
        CommentDto(
            id=1,
            commented_by_id=2,
            post_id=2,
            comment_content="nice post",
            commented_at=datetime.datetime(2020, 5, 20, 0, 0),
            parent_comment_id=None
        ),
        CommentDto(
            id=2,
            commented_by_id=1,
            post_id=2,
            comment_content="thank you",
            commented_at=datetime.datetime(2020, 5, 20, 0, 0),
            parent_comment_id=1
        ),
    ]
    comment_reaction_metrics_dto = [
        CommentReactionMetricsDto(
            comment_id = 1,
            reactions_count = 0,
            reactions_list =  []
        ),
        CommentReactionMetricsDto(
            comment_id = 2,
            reactions_count = 0,
            reactions_list =  []
        )
    ]
    comment_replies_count_dtos = [
        CommentRepliesCountDto(
            comment_id = 1,
            replies_count = 1
        )
    ]
    reaction_dtos = [
    ]
    user_dtos = [
        UserDto(
            id=1,
            name="Anusha",
            profile_pic="avatar.png",
        ),
        UserDto(
            id=2,
            name="Sneha",
            profile_pic="avatar.png",
        ),
    ]
    post_dto = \
        PostDto(
            id=2,
            posted_by_id=1,
            post_content="My second post",
            posted_at=datetime.datetime(2020, 5, 20, 0, 0),
        ),
    all_fields = {
        "post_dto": post_dto,
        "user_dtos": user_dtos,
        "comment_dtos": comment_dtos,
        "reaction_dtos": reaction_dtos,
        "post_reactions_dto": post_reactions_dto,
        "post_comments_count_dto": post_comments_count_dto,
        "comment_reaction_metrics_dto": comment_reaction_metrics_dto,
        "comment_replies_count_dtos": comment_replies_count_dtos
    }
    return all_fields

@pytest.fixture()
def multiple_repeated_reactions_for_comments():
    all_fields = {}
    post_reactions_dto = PostReactionsDto(
        post_id=2,
        reactions_count = 0,
        reactions_list = [],
    )
    post_comments_count_dto = PostCommentCountDto(
        post_id=2,
        comments_count = 1
    )
    comment_dtos = [
        CommentDto(
            id=1,
            commented_by_id=2,
            post_id=2,
            comment_content="nice post",
            commented_at=datetime.datetime(2020, 5, 20, 0, 0),
            parent_comment_id=None
        ),
        CommentDto(
            id=2,
            commented_by_id=1,
            post_id=2,
            comment_content="thank you",
            commented_at=datetime.datetime(2020, 5, 20, 0, 0),
            parent_comment_id=1
        ),
    ]
    comment_reaction_metrics_dto = [
        CommentReactionMetricsDto(
            comment_id = 1,
            reactions_count = 3,
            reactions_list =  ["WOW","HAHA"]
        ),
        CommentReactionMetricsDto(
            comment_id = 2,
            reactions_count = 0,
            reactions_list =  []
        )
    ]
    comment_replies_count_dtos = [
        CommentRepliesCountDto(
            comment_id = 1,
            replies_count = 1
        )
    ]
    reaction_dtos = [
        ReactionDto(
            id=1,
            post_id=None,
            reacted_by_id=1,
            reaction=ReactionType.WOW.value,
            comment_id=1
        ),
        ReactionDto(
            id=2,
            post_id=None,
            reacted_by_id=2,
            reaction=ReactionType.WOW.value,
            comment_id=1
        ),
        ReactionDto(
            id=3,
            comment_id=1,
            post_id=None,
            reacted_by_id=3,
            reaction=ReactionType.HAHA.value
        ),
    ]
    user_dtos = [
        UserDto(
            id=1,
            name="Anusha",
            profile_pic="avatar.png",
        ),
        UserDto(
            id=2,
            name="Sneha",
            profile_pic="avatar.png",
        ),
    ]
    post_dto = \
        PostDto(
            id=2,
            posted_by_id=1,
            post_content="My second post",
            posted_at=datetime.datetime(2020, 5, 20, 0, 0),
        ),
    all_fields = {
        "post_dto": post_dto,
        "user_dtos": user_dtos,
        "comment_dtos": comment_dtos,
        "reaction_dtos": reaction_dtos,
        "post_reactions_dto": post_reactions_dto,
        "post_comments_count_dto": post_comments_count_dto,
        "comment_reaction_metrics_dto": comment_reaction_metrics_dto,
        "comment_replies_count_dtos": comment_replies_count_dtos
    }
    return all_fields

@pytest.fixture()
def post_with_one_comment_with_one_reply_and_reply_to_reply():
    all_fields = {}
    post_reactions_dto = PostReactionsDto(
        post_id=2,
        reactions_count = 0,
        reactions_list = [],
    )
    post_comments_count_dto = PostCommentCountDto(
        post_id=2,
        comments_count = 1
    )
    comment_dtos = [
        CommentDto(
            id=1,
            commented_by_id=2,
            post_id=2,
            comment_content="nice post",
            commented_at=datetime.datetime(2020, 5, 20, 0, 0),
            parent_comment_id=None
        ),
        CommentDto(
            id=2,
            commented_by_id=1,
            post_id=2,
            comment_content="thank you",
            commented_at=datetime.datetime(2020, 5, 20, 0, 0),
            parent_comment_id=1
        ),
        CommentDto(
            id=3,
            commented_by_id=2,
            post_id=2,
            comment_content="you are welcome",
            commented_at=datetime.datetime(2020, 5, 20, 0, 0),
            parent_comment_id=1
        ),
    ]
    comment_reaction_metrics_dto = [
        CommentReactionMetricsDto(
            comment_id = 1,
            reactions_count = 0,
            reactions_list =  []
        ),
        CommentReactionMetricsDto(
            comment_id = 2,
            reactions_count = 0,
            reactions_list =  []
        ),
        CommentReactionMetricsDto(
            comment_id = 3,
            reactions_count = 0,
            reactions_list =  []
        )
    ]
    comment_replies_count_dtos = [
        CommentRepliesCountDto(
            comment_id = 1,
            replies_count = 2
        )
    ]
    reaction_dtos = []
    user_dtos = [
        UserDto(
            id=1,
            name="Anusha",
            profile_pic="avatar.png",
        ),
        UserDto(
            id=2,
            name="Sneha",
            profile_pic="avatar.png",
        ),
    ]
    post_dto = \
        PostDto(
            id=2,
            posted_by_id=1,
            post_content="My second post",
            posted_at=datetime.datetime(2020, 5, 20, 0, 0),
        ),
    all_fields = {
        "post_dto": post_dto,
        "user_dtos": user_dtos,
        "comment_dtos": comment_dtos,
        "reaction_dtos": reaction_dtos,
        "post_reactions_dto": post_reactions_dto,
        "post_comments_count_dto": post_comments_count_dto,
        "comment_reaction_metrics_dto": comment_reaction_metrics_dto,
        "comment_replies_count_dtos": comment_replies_count_dtos
    }
    return all_fields

@pytest.fixture()
def comment_reaction_metrics_dto():
    comment_reaction_metrics_dto = [
        CommentReactionMetricsDto(
            comment_id = 1,
            reactions_count = 1,
            reactions_list = ["SAD"]
        ),
        CommentReactionMetricsDto(
            comment_id = 2,
            reactions_count = 0,
            reactions_list =  []
        ),
        CommentReactionMetricsDto(
            comment_id = 3,
            reactions_count = 0,
            reactions_list =  []
        ),
    ]
    return comment_reaction_metrics_dto

@pytest.fixture()
def comment_replies_count_dtos():
    comment_replies_count_dtos = [
        CommentRepliesCountDto(
            comment_id = 1,
            replies_count = 2
        )
    ]
    return comment_replies_count_dtos
    

@pytest.fixture()
def get_post_response():
    get_post_response = {
        'post_content': 'My first post',
        'post_id': 1,
        'posted_at': '20-5-2020,00:00:1568140200.00',
        'posted_by': {
            'name': 'Anusha',
            'profile_pic': 'avatar.png',
            'user_id': 1
        },
        'reactions': {
            'count': 2,
            'type': [
                'HAHA',
                'LIKE'
            ]
        },
        'comments': [
            {
                'comment_content': 'nice post',
                'comment_id': 1,
                'commented_at': '20-5-2020,00:00:1568140200.00',
                'commenter': {
                    'name': 'sneha',
                    'profile_pic': 'avatar',
                    'user_id': 2
                },
                'reactions': {
                    'count': 1,
                    'type': [
                        'SAD'
                    ]
                },
                'replies': [
                    {
                        'comment_content': 'reply to comment',
                        'comment_id': 2,
                        'commented_at': '20-5-2020,00:00:1568140200.00',
                        'commenter': {
                            'name': 'Anusha',
                            'profile_pic': 'avatar.png',
                            'user_id': 1
                        },
                        'reactions': {
                            'count': 0,
                            'type': []
                        }
                    },
                    {
                        'comment_content': 'reply to reply',
                        'comment_id': 3,
                        'commented_at': '20-5-2020,00:00:1568140200.00',
                        'commenter': {
                            'name': 'Sneha',
                            'profile_pic': 'avatar.png',
                            'user_id': 2
                        },
                        'reactions': {
                            'count': 0,
                            'type': []
                        }
                    },
                    
                ],
                'replies_count': 2
            }

        ],
        "comments_count": 1
    }
    return get_post_response


@pytest.fixture()
def get_user_posts_response():
    get_user_posts_response = [
        {
            'post_content': 'My first post',
            'post_id': 1,
            'posted_at': '20-5-2020,00:00:1568140200.00',
            'posted_by': {
                'name': 'Anusha',
                'profile_pic': 'avatar.png',
                'user_id': 1
            },
            'reactions': {
                'count': 2,
                'type': [
                    'HAHA',
                    'LIKE'
                ]
            },
            'comments': [
                {
                    'comment_content': 'nice post',
                    'comment_id': 1,
                    'commented_at': '20-5-2020,00:00:1568140200.00',
                    'commenter': {
                        'name': 'sneha',
                        'profile_pic': 'avatar',
                        'user_id': 2
                    },
                    'reactions': {
                        'count': 1,
                        'type': [
                            'SAD'
                        ]
                    },
                    'replies': [
                        {
                            'comment_content': 'reply to comment',
                            'comment_id': 2,
                            'commented_at': '20-5-2020,00:00:1568140200.00',
                            'commenter': {
                                'name': 'Anusha',
                                'profile_pic': 'avatar.png',
                                'user_id': 1
                            },
                            'reactions': {
                                'count': 0,
                                'type': []
                            }
                        },
                        {
                            'comment_content': 'reply to reply',
                            'comment_id': 3,
                            'commented_at': '20-5-2020,00:00:1568140200.00',
                            'commenter': {
                                'name': 'Sneha',
                                'profile_pic': 'avatar.png',
                                'user_id': 2
                            },
                            'reactions': {
                                'count': 0,
                                'type': []
                            }
                        },
                    ],
                    'replies_count': 2
                }
            ],
            "comments_count": 1
        },
        {
            'post_content': 'My second post',
            'post_id': 2,
            'posted_at': '20-5-2020,00:00:1568140200.00',
            'posted_by': {
                'name': 'Anusha',
                'profile_pic': 'avatar.png',
                'user_id': 1
            },
            'reactions': {
                'count': 0,
                'type': []
            },
            'comments': [],
            "comments_count": 0
        }
    ]
    return get_user_posts_response


@pytest.fixture
def get_comment_replies_response():
    comment_replies_response = [
        {
            'comment_content': 'reply to comment',
            'comment_id': 2,
            'commented_at': '20-5-2020,00:00:1568140200.00',
            'commenter': {
                'name': 'Anusha',
                'profile_pic': 'avatar.png',
                'user_id': 1
            },
        },
        {
            'comment_content': 'reply to reply',
            'comment_id': 3,
            'commented_at': '20-5-2020,00:00:1568140200.00',
            'commenter': {
                'name': 'Sneha',
                'profile_pic': 'avatar.png',
                'user_id': 2
            },
        },
    ]
    return comment_replies_response