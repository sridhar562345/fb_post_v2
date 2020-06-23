from rest_framework import serializers
from fb_post_v2.build.serializers.definitions.UserWithReaction.UserWithReactionSerializer import UserWithReactionSerializer

class Status_200Serializer(serializers.ListSerializer):
    child = UserWithReactionSerializer()
