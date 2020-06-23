class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"post_id": 1, "posted_by": {"user_id": 1, "name": "string", "profile_pic": "string"}, "posted_at": "2099-12-31 00:00:00", "post_content": "string", "reactions": {"count": 1, "type": ["WOW"]}, "comments": [{"comment_id": 1, "commenter": {"user_id": 1, "name": "string", "profile_pic": "string"}, "commented_at": "2099-12-31 00:00:00", "comment_content": "string", "reactions": {"count": 1, "type": ["WOW"]}, "replies_count": 1, "replies": [{"comment_id": 1, "commenter": {"user_id": 1, "name": "string", "profile_pic": "string"}, "commented_at": "2099-12-31 00:00:00", "comment_content": "string", "reactions": {"count": 1, "type": ["WOW"]}}]}]}',
            "response_serializer": "PostSerializer",
            "response_serializer_import_str": "from fb_post_v2.build.serializers.definitions.Post.PostSerializer import PostSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass