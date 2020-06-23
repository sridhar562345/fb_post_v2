# pylint: disable=wrong-import-position

APP_NAME = "fb_post_v2"
OPERATION_NAME = "total_reactions_count"
REQUEST_METHOD = "get"
URL_SUFFIX = "reactions/count/v1/"

from .test_case_01 import TestCase01TotalReactionsCountAPITestCase

__all__ = [
    "TestCase01TotalReactionsCountAPITestCase"
]
