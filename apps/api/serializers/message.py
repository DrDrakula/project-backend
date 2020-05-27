# DRF
from rest_framework import pagination
from rest_framework.response import Response
# Models
from apps.api.models import Message
# Serializers
from apps.api.serializers.base_serializers import BaseSerializer
from apps.api.serializers import UserSerializer, ChatroomSerializer

class MessageSerializer(BaseSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class SingleMessageSerializer(BaseSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()
    chatroom = ChatroomSerializer()

    class Meta:
        model = Message
        fields = '__all__'

class MessagePagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })