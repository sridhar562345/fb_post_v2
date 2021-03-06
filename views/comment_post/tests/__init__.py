# pylint: disable=wrong-import-position

APP_NAME = "fb_post_v2"
OPERATION_NAME = "comment_post"
REQUEST_METHOD = "post"
URL_SUFFIX = "posts/{post_id}/comment/create/v1/"

from .test_case_01 import TestCase01CommentPostAPITestCase

__all__ = [
    "TestCase01CommentPostAPITestCase"
]
