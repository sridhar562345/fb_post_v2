from rest_framework import serializers

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_object
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_list_object
from django_swagger_utils.drf_server.fields.collection_format_field import CollectionFormatField


class GetCommentIdResponseType(object):
    def __init__(self, comment_id=None,  **kwargs):
        self.comment_id = comment_id

    def __str__(self):
        from django_swagger_utils.drf_server.utils.server_gen.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class GetCommentIdResponseSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField(required=False, allow_null=True)

    def create(self, validated_data):
        return GetCommentIdResponseType(**validated_data)
