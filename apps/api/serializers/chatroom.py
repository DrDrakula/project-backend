# DRF
from rest_framework import pagination
from rest_framework.response import Response
# Models
from apps.api.models import Chatroom
# Serializers
from apps.api.serializers.base_serializers import BaseSerializer

class ChatroomSerializer(BaseSerializer):
    class Meta:
        model = Chatroom
        fields = '__all__'

class ChatroomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })