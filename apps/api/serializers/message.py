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