from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
from fb_post_v2.constants.enums import ReactionType

@dataclass
class UserDto:
    id: int
    name: str
    profile_pic: str

@dataclass
class PostDto:
    id: int
    posted_by_id: int
    post_content: str
    posted_at: datetime

@dataclass
class CommentDto:
    id: int
    commented_by_id: int
    post_id: int
    comment_content: str
    commented_at: datetime
    parent_comment_id: Optional[int]


@dataclass
class ReactionDto:
    id: int
    comment_id: Optional[int]
    post_id: Optional[int]
    reacted_by_id: int
    reaction: ReactionType


@dataclass
class PostReactionCompleteDetailsDto:
    user_dtos: List[UserDto]
    reaction_dtos: List[ReactionDto]

@dataclass
class CommentRepliesDto:
    users_dto: List[UserDto]
    comments_dto: List[CommentDto]


@dataclass
class PostCompleteDetailsDto:
    post_dto: PostDto
    users_dto: List[UserDto]
    comments_dto: List[CommentDto]
    reactions_dto: List[ReactionDto]


@dataclass
class UserPostDetailsDto:
    post_dto: List[PostDto]
    users_dto: List[UserDto]
    comments_dto: List[CommentDto]
    reactions_dto: List[ReactionDto]

@dataclass
class PostReactionsDto:
    post_id: int
    reactions_count: int
    reactions_list: List[ReactionType]

@dataclass
class PostCommentCountDto:
    post_id: int
    comments_count: int

@dataclass
class CommentReactionMetricsDto:
    comment_id: int
    reactions_count: int
    reactions_list: List[ReactionType]

@dataclass
class CommentRepliesCountDto:
    comment_id: int
    replies_count: int

@dataclass
class PostCompleteDto:
    post_details_dto: PostCompleteDetailsDto
    post_reactions_dto: PostReactionsDto
    post_comments_count_dto: PostCommentCountDto
    comment_reactions_dtos: List[CommentReactionMetricsDto]
    comment_replies_count_dtos: List[CommentRepliesCountDto]

@dataclass
class UserPostsCompleteDto:
    user_post_details_dto: UserPostDetailsDto
    post_reactions_dtos: List[PostReactionsDto]
    post_comments_count_dtos: List[PostCommentCountDto]
    comment_reactions_dtos: List[CommentReactionMetricsDto]
    comment_replies_count_dtos: List[CommentRepliesCountDto]
