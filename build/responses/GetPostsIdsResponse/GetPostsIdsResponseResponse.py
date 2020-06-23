class GetPostsIdsResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '[1]',
            "response_serializer": "GetPostsIdsResponseSerializer",
            "response_serializer_import_str": "from fb_post_v2.build.responses.GetPostsIdsResponse.GetPostsIdsResponse.GetPostsIdsResponseSerializer import GetPostsIdsResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass