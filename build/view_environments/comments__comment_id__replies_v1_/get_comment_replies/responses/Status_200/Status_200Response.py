class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '[{"comment_id": 1, "commenter": {"user_id": 1, "name": "string", "profile_pic": "string"}, "commented_at": "2099-12-31 00:00:00", "comment_content": "string"}]',
            "response_serializer": "Status_200Serializer",
            "response_serializer_import_str": "from fb_post_v2.build.view_environments.comments__comment_id__replies_v1_.get_comment_replies.responses.Status_200.Status_200.Status_200Serializer import Status_200Serializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass