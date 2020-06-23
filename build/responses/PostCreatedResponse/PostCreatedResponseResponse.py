class PostCreatedResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"post_id": 1}',
            "response_serializer": "PostCreatedResponseSerializer",
            "response_serializer_import_str": "from fb_post_v2.build.responses.PostCreatedResponse.PostCreatedResponse.PostCreatedResponseSerializer import PostCreatedResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass