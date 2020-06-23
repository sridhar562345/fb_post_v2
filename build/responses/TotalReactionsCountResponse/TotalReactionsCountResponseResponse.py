class TotalReactionsCountResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"count": 1}',
            "response_serializer": "TotalReactionsCountResponseSerializer",
            "response_serializer_import_str": "from fb_post_v2.build.responses.TotalReactionsCountResponse.TotalReactionsCountResponse.TotalReactionsCountResponseSerializer import TotalReactionsCountResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass