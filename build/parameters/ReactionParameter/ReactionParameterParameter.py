class ReactionTypeParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "ReactionParameter",
            "parameter_field_name": "reaction_type"
        }
        return param_names

    @staticmethod
    def get_serializer_class():
        serializer_options = {
            "param_serializer": "reactionSerializer",
            "param_serializer_import_str": "from fb_post_v2.build.serializers.definitions.reaction.reactionSerializer import reactionSerializer",
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