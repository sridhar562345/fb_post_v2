# pylint: disable=wrong-import-position

APP_NAME = "fb_post_v2"
OPERATION_NAME = "user_posts"
REQUEST_METHOD = "get"
URL_SUFFIX = "reacted/posts/"

from .test_case_01 import TestCase01UserPostsAPITestCase

__all__ = [
    "TestCase01UserPostsAPITestCase"
]
