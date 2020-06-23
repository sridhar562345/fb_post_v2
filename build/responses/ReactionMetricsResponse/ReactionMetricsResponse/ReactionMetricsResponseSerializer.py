from rest_framework import serializers
from fb_post_v2.build.serializers.definitions.reactionMetrics.reactionMetricsSerializer import reactionMetricsSerializer

class ReactionMetricsResponseSerializer(serializers.ListSerializer):
    child = reactionMetricsSerializer()
