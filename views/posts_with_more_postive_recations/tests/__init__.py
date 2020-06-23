# pylint: disable=wrong-import-position

APP_NAME = "fb_post_v2"
OPERATION_NAME = "posts_with_more_postive_recations"
REQUEST_METHOD = "get"
URL_SUFFIX = "more/postive/reactions/posts/v1/"

from .test_case_01 import TestCase01PostsWithMorePostiveRecationsAPITestCase

__all__ = [
    "TestCase01PostsWithMorePostiveRecationsAPITestCase"
]
