# django
from django.contrib.auth import get_user_model
# drf
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):

    modified_by = serializers.HyperlinkedRelatedField(
        allow_null=True,
        required=False,
        view_name='user-detail',
        read_only=True,
        default=None,)

    is_active = serializers.BooleanField(
        read_only=True,
        default=True
    )

    modified_count = serializers.IntegerField(
        read_only=True,
        default=0
    )

    password = serializers.CharField(
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = (
                  'url',
                  'id',
                  'username',
                  'email',
                  'password',
                  'first_name',
                  'last_name',
                  'last_login',
                  'created_date',
                  'modified_date',
                  'modified_count',
                  'modified_by',
                  'is_active',
                  'is_locked',
                  'is_superuser',
                  'is_staff',
                  )