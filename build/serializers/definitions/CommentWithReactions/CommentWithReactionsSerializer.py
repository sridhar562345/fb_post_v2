from fb_post_v2.build.serializers.definitions.Comment.CommentSerializer import CommentSerializer
from fb_post_v2.build.serializers.definitions.Comment.CommentSerializer import CommentType
from fb_post_v2.build.serializers.definitions.CommentWithReactions.CommentWithReactions.Schema1.Schema1Serializer import Schema1Serializer
from fb_post_v2.build.serializers.definitions.CommentWithReactions.CommentWithReactions.Schema1.Schema1Serializer import Schema1Type

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize

class CommentWithReactionsType(CommentType, Schema1Type):
    def __init__(self, **validated_data):
        CommentType.__init__(self, **validated_data)
        Schema1Type.__init__(self, **validated_data)
        

class CommentWithReactionsSerializer(CommentSerializer, Schema1Serializer):
    def create(self, validated_data):
        
        commentSerializer, _ = deserialize(CommentSerializer, validated_data, many=False, partial=True)
        validated_data.update(commentSerializer.__dict__)
        
        schema1Serializer, _ = deserialize(Schema1Serializer, validated_data, many=False, partial=True)
        validated_data.update(schema1Serializer.__dict__)
        
        return CommentWithReactionsType(**validated_data)
