class ReactionMetricsResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '[{"reaction_type": "WOW", "count": 1}]',
            "response_serializer": "ReactionMetricsResponseSerializer",
            "response_serializer_import_str": "from fb_post_v2.build.responses.ReactionMetricsResponse.ReactionMetricsResponse.ReactionMetricsResponseSerializer import ReactionMetricsResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass