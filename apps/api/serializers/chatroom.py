# Models
from apps.api.models import Chatroom
# Serializers
from apps.api.serializers.base_serializers import BaseSerializer

class ChatroomSerializer(BaseSerializer):
    class Meta:
        model = Chatroom
        fields = '__all__'