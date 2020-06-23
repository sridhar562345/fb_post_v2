from rest_framework import serializers

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_object
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_list_object
from django_swagger_utils.drf_server.fields.collection_format_field import CollectionFormatField


class Schema1Type(object):
    def __init__(self, reactions, replies_count, replies,  **kwargs):
        self.reactions = reactions
        self.replies_count = replies_count
        self.replies = replies

    def __str__(self):
        from django_swagger_utils.drf_server.utils.server_gen.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class Schema1Serializer(serializers.Serializer):
    from fb_post_v2.build.serializers.definitions.Reaction.ReactionSerializer import ReactionSerializer
    reactions = ReactionSerializer(allow_null=True)
    replies_count = serializers.IntegerField()
    from fb_post_v2.build.serializers.definitions.CommentWithReactions.CommentWithReactionsSerializer import CommentWithReactionsSerializer
    replies = CommentWithReactionsSerializer(many=True)

    def create(self, validated_data):
        from fb_post_v2.build.serializers.definitions.Reaction.ReactionSerializer import ReactionSerializer
        reactions_val, _ = deserialize(ReactionSerializer, validated_data.pop("reactions", None), many=False, partial=True)
        
        from fb_post_v2.build.serializers.definitions.CommentWithReactions.CommentWithReactionsSerializer import CommentWithReactionsSerializer
        replies_val = []
        replies_list_val = validated_data.pop("replies", [])
        for each_data in replies_list_val:
            each_obj, _ = deserialize(CommentWithReactionsSerializer, each_data, many=False, partial=True)
            replies_val.append(each_obj)
        
        return Schema1Type(reactions=reactions_val, replies=replies_val, **validated_data)
