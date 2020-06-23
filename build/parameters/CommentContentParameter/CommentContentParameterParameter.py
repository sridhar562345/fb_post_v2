class CommentContentParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "CommentContentParameter",
            "parameter_field_name": "comment_content"
        }
        return param_names

    @staticmethod
    def get_serializer_class():
        serializer_options = {
            "param_serializer": "comment_contentSerializer",
            "param_serializer_import_str": "from fb_post_v2.build.parameters.CommentContentParameter.comment_content.comment_contentSerializer import comment_contentSerializer",
            "param_serializer_required": True,
            "param_serializer_array": False
        }
        return serializer_options
        

    @staticmethod
    def get_serializer_field():
        pass

    @staticmethod
    def get_url_regex():
        pass