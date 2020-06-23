class ReplyContentParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "ReplyContentParameter",
            "parameter_field_name": "reply_content"
        }
        return param_names

    @staticmethod
    def get_serializer_class():
        serializer_options = {
            "param_serializer": "reply_contentSerializer",
            "param_serializer_import_str": "from fb_post_v2.build.parameters.ReplyContentParameter.reply_content.reply_contentSerializer import reply_contentSerializer",
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