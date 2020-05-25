import uuid
# django
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
# models
from apps.api.models.BaseModel import BaseModel
# from apps.api.manager import UserManager


class Chatroom(BaseModel):
    
    name = models.CharField(_('name'),
                            max_length=255,
                            blank=False,
                            db_index=True
                            )

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   blank=True,
                                   null=True,
                                   editable=False,
                                   db_index=True,
                                   related_name='chatrooms_created',
                                   )

    class Meta:
        app_label = 'api'
        verbose_name = _('chatroom')
        verbose_name_plural = _('chatrooms')

    def __str__(self):
        return f'{self.name}'