"""
create comment given valid data
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post_v2.factories.factories import PostFactor

REQUEST_BODY = """
{
    "comment_content": "string"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"post_id": 1},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["read", "write"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase02CommentPostAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase02CommentPostAPITestCase, self).setupUser(
            username=username, password=password
        )
        PostFactor.create()
        print("*************")
        print(self.foo_user.id)
        print("*" * 10)
    
    def test_case(self):
        response = self.default_test_case()
        
        import json
        
        response_content = json.loads(response.content)
        comment_id = response_content['comment_id']
        
        from fb_post_v2.models import Comment

        comment = Comment.objects.get(id=comment_id)
        
        self.assert_match_snapshot(
            name='user_id',
            value=comment.commented_by_id
        )
        
        self.assert_match_snapshot(
            name='post_id',
            value=comment.post_id
        )
        
        self.assert_match_snapshot(
            name='comment_content',
            value=comment.content
        )
        