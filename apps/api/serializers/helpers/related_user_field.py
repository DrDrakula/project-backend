# dango
from django.contrib.auth import get_user_model
# drf
from rest_framework import serializers
from rest_framework.reverse import reverse

User = get_user_model()

class RelatedUserField(serializers.RelatedField):
    """serial.CurrentUserDefault() stopped working once Elasticsearch was
    implemented so I created my own custom serializer field that automattically
    sets the user for created_by and modified_by
    """
    queryset = User.objects.all()

    def to_representation(self, value):
        """How the value is displayed"""
        view_name = 'user-detail'
        url_kwargs = {'pk': value.id}
        request = self.context['request']
        return reverse(view_name, kwargs=url_kwargs, request=request)

    def to_internal_value(self, data):
        """Sets the value of the data in the serializer"""
        user = self.context['request'].user
        # From drf frontend the user object is wrapped by SimpleLazyObject
        if hasattr(user, '_wrapped'):
            return user._wrapped
        # From Client user object is not wrapped
        return user