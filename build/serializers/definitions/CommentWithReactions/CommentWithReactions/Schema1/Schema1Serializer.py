from rest_framework import serializers

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_object
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_list_object
from django_swagger_utils.drf_server.fields.collection_format_field import CollectionFormatField


class Schema1Type(object):
    def __init__(self, reactions,  **kwargs):
        self.reactions = reactions

    def __str__(self):
        from django_swagger_utils.drf_server.utils.server_gen.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class Schema1Serializer(serializers.Serializer):
    from fb_post_v2.build.serializers.definitions.Reaction.ReactionSerializer import ReactionSerializer
    reactions = ReactionSerializer(allow_null=True)

    def create(self, validated_data):
        from fb_post_v2.build.serializers.definitions.Reaction.ReactionSerializer import ReactionSerializer
        reactions_val, _ = deserialize(ReactionSerializer, validated_data.pop("reactions", None), many=False, partial=True)
        
        return Schema1Type(reactions=reactions_val, **validated_data)
