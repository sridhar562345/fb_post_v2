# pylint: disable=wrong-import-position

APP_NAME = "fb_post_v2"
OPERATION_NAME = "react_post"
REQUEST_METHOD = "post"
URL_SUFFIX = "posts/{post_id}/react/v1/"

from .test_case_01 import TestCase01ReactPostAPITestCase

__all__ = [
    "TestCase01ReactPostAPITestCase"
]
