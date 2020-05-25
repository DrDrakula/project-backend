import uuid
# django
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
# models
from apps.api.models.BaseModel import BaseModel
# from apps.api.manager import UserManager


class User(AbstractUser, BaseModel):
    # Use UUID to make the merging of tables much easier if need be.
    id = models.UUIDField(primary_key=True,
                          editable=False,
                          default=uuid.uuid4,
                          verbose_name='public identifier',)
    email = models.EmailField(_('email address'), unique=True, blank=False)

    modified_by = models.ForeignKey('self',
                                    # on_delete=models.SET(BaseModel.get_sentinel_user),
                                    on_delete=models.CASCADE,
                                    db_index=True,
                                    null=True,
                                    blank=True,
                                    default=None,
                                    related_name='modified_users'
                                    )

    is_manager = models.BooleanField(default=False,
                                     help_text=f"Describes user's role")

    group = models.TextField(default=False,
                             max_length=15,
                             blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        app_label = 'api'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        if self.get_full_name():
            return f'{self.get_full_name()}'
        return f'{self.username}'