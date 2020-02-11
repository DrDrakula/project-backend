# drf
from rest_framework import serializers
# helpers
from apps.api.serializers.helpers import RelatedUserField


class BaseSerializer(serializers.HyperlinkedModelSerializer):
    def get_field_names(self, declared_fields, info):
        expanded_fields = super(
            BaseSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields

    is_active = serializers.BooleanField(
        read_only=True,
        default=True,
    )

    is_locked = serializers.BooleanField(
        read_only=True,
        default=False,
    )

    modified_count = serializers.IntegerField(
        read_only=True,
        default=0
    )

    class Meta:
        fields = '__all__'
        extra_fields=()


class UserSerializerMixin(serializers.HyperlinkedModelSerializer):
    created_by = RelatedUserField()

    modified_by = serializers.HyperlinkedRelatedField(
        allow_null=True,
        required=False,
        view_name='user-detail',
        read_only=True,
        default=None,
        )