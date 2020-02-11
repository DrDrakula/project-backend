from django.contrib.auth import get_user_model
from rest_auth.serializers import UserDetailsSerializer as UserDetails


User = get_user_model()


class UserDetailsSerializer(UserDetails):
    """Custom UserDetailsSerializer."""

    class Meta(UserDetails.Meta):
        model = User
        fields = UserDetails.Meta.fields + ('url',)