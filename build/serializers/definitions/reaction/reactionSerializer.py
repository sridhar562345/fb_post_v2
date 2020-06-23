from rest_framework import serializers

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_object
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_list_object
from django_swagger_utils.drf_server.fields.collection_format_field import CollectionFormatField


class reactionType(object):
    def __init__(self, reaction_type=None,  **kwargs):
        self.reaction_type = reaction_type

    def __str__(self):
        from django_swagger_utils.drf_server.utils.server_gen.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class reactionSerializer(serializers.Serializer):
    reaction_type = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return reactionType(**validated_data)
