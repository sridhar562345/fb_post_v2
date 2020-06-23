from rest_framework import serializers

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_object
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_list_object
from django_swagger_utils.drf_server.fields.collection_format_field import CollectionFormatField


class Status_200Type(object):
    def __init__(self, posts=None, total_posts=None,  **kwargs):
        self.posts = posts
        self.total_posts = total_posts

    def __str__(self):
        from django_swagger_utils.drf_server.utils.server_gen.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class Status_200Serializer(serializers.Serializer):
    from fb_post_v2.build.serializers.definitions.Post.PostSerializer import PostSerializer
    posts = PostSerializer(required=False, many=True)
    total_posts = serializers.IntegerField(required=False, allow_null=True)

    def create(self, validated_data):
        from fb_post_v2.build.serializers.definitions.Post.PostSerializer import PostSerializer
        posts_val = []
        posts_list_val = validated_data.pop("posts", [])
        for each_data in posts_list_val:
            each_obj, _ = deserialize(PostSerializer, each_data, many=False, partial=True)
            posts_val.append(each_obj)
        
        return Status_200Type(posts=posts_val, **validated_data)
