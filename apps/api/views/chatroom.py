# DRF
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
# Models
from apps.api.models import Chatroom
# Serializers
from apps.api.serializers import ChatroomSerializer

class ChatroomViewSet(viewsets.ModelViewSet):
    queryset = Chatroom.objects.all().order_by('name')
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)

    serializer_class = ChatroomSerializer

    permission_classes = [IsAuthenticated, ]