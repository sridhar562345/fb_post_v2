from rest_framework import serializers
from fb_post_v2.build.serializers.definitions.Comment.CommentSerializer import CommentSerializer

class Status_200Serializer(serializers.ListSerializer):
    child = CommentSerializer()
