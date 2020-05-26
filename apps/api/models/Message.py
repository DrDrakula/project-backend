import uuid
# django
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
# models
from apps.api.models.BaseModel import BaseModel
from apps.api.models.Chatroom import Chatroom
# from apps.api.manager import UserManager


class Message(BaseModel):
    message = models.CharField(_('message'),
                            max_length=255,
                            blank=False,
                            db_index=True
                            )

    sender = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   blank=False,
                                   null=False,
                                   related_name='messages_sent',
                                   )

    receiver = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   blank=True,
                                   null=True,
                                   related_name='messages_received',
                                   )

    chatroom = models.ForeignKey(Chatroom,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True,
                                 related_name='messages')    

    class Meta:
        app_label = 'api'
        verbose_name = _('message')
        verbose_name_plural = _('messages')

    def __str__(self):
        return f'{self.message}'