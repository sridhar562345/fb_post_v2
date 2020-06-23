class CommentIdParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "CommentIdParameter",
            "parameter_field_name": "comment_id"
        }
        return param_names

    @staticmethod
    def get_serializer_class():
        pass

    @staticmethod
    def get_serializer_field():
        pass

    @staticmethod
    def get_url_regex():
        regex = r"(?P<comment_id>\d+)"
        return regex