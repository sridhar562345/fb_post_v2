from rest_framework import serializers


class GetPostsIdsResponseSerializer(serializers.ListSerializer):
    child = serializers.IntegerField()
