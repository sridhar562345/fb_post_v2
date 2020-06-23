"""
# create comment invalid post id 
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "comment_content": "string"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"post_id": 1234},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["read", "write"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01CommentPostAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01CommentPostAPITestCase, self).setupUser(
            username=username, password=password
        )
        
        print("*************")
        print(self.foo_user.id)
        print("*" * 10)
    
    def test_case(self):
        self.default_test_case()