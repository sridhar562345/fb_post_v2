class LimitParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "LimitParameter",
            "parameter_field_name": "limit"
        }
        return param_names

    @staticmethod
    def get_serializer_class():
        pass

    @staticmethod
    def get_serializer_field():
        from rest_framework import serializers
        from django_swagger_utils.drf_server.fields.collection_format_field import CollectionFormatField
        return serializers.IntegerField(help_text="display limit no of posts")
        

    @staticmethod
    def get_url_regex():
        pass