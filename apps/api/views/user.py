# Django
from django.contrib.auth import get_user_model
# DRF
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
# Serializers
from apps.api.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('last_name')
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)

    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated, ]