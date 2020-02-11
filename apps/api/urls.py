# django
# from django.conf import settings
from django.contrib import admin
from django.urls import path, include
# drf
from rest_framework import routers
# views
from apps.api import views  # make sure to add new views to __init__.py

router = routers.DefaultRouter()

router.register(r'users',
                views.UserViewSet,
                basename='user'
                )

urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_auth.urls')),
    path('register/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls)
    ]