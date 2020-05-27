# DRF
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters, permissions, status
from rest_framework.response import Response
# Models
from apps.api.models import Message
# Serializers
from apps.api.serializers import MessageSerializer, SingleMessageSerializer, MessagePagination

class StandardResultsSetPagination(MessagePagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('created_date')
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)

    permission_classes = [IsAuthenticated, ]

    def retrieve(self, request, pk=None):
        try:
            message = Message.objects.get(pk=pk)
            serialized_message = SingleMessageSerializer(message, context={'request': request})
            return Response(serialized_message.data, status=status.HTTP_200_OK)
        except:
            return Response({'message': "Message not found."}, status=status.HTTP_404_NOT_FOUND)

    pagination_class = StandardResultsSetPagination
    serializer_class = MessageSerializer
