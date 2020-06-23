class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '[{"user_id": 1, "name": "string", "profile_pic": "string", "reaction": "string"}]',
            "response_serializer": "Status_200Serializer",
            "response_serializer_import_str": "from fb_post_v2.build.view_environments.posts__post_id__reactions_v1_.get_post_reactions.responses.Status_200.Status_200.Status_200Serializer import Status_200Serializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass