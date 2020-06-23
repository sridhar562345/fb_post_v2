class GetCommentIdResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"comment_id": 1}',
            "response_serializer": "GetCommentIdResponseSerializer",
            "response_serializer_import_str": "from fb_post_v2.build.responses.GetCommentIdResponse.GetCommentIdResponse.GetCommentIdResponseSerializer import GetCommentIdResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass