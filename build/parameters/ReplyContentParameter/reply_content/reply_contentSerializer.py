from rest_framework import serializers

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_object
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_list_object
from django_swagger_utils.drf_server.fields.collection_format_field import CollectionFormatField


class reply_contentType(object):
    def __init__(self, reply_content=None,  **kwargs):
        self.reply_content = reply_content

    def __str__(self):
        from django_swagger_utils.drf_server.utils.server_gen.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class reply_contentSerializer(serializers.Serializer):
    reply_content = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return reply_contentType(**validated_data)
