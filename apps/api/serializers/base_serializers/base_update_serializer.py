# drf
from rest_framework import serializers
# helpers
from apps.api.serializers.helpers import RelatedUserField


class BaseUpdateSerializer(serializers.HyperlinkedModelSerializer):
    modified_by = RelatedUserField()

    modified_count = serializers.IntegerField(
        read_only=True,
    )