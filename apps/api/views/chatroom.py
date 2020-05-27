# DRF
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
# Models
from apps.api.models import Chatroom
# Serializers
from apps.api.serializers import ChatroomSerializer, ChatroomPagination

class StandardResultsSetPagination(ChatroomPagination):
    page_size = 40
    page_size_query_param = 'page_size'
    max_page_size = 40

class ChatroomViewSet(viewsets.ModelViewSet):
    queryset = Chatroom.objects.all().order_by('name')
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)

    serializer_class = ChatroomSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated, ]