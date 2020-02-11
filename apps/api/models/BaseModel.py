import uuid
# django
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth import get_user_model

class BaseModel(models.Model):
    # Use UUID to make the merging of tables much easier if need be.
    id = models.UUIDField(primary_key=True,
                          editable=False,
                          default=uuid.uuid4,
                          verbose_name='public identifier',)

    created_date = models.DateTimeField(_('created date'),
                                        auto_now_add=True,
                                        editable=False)
    modified_date = models.DateTimeField(_('modified date'), auto_now=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_locked = models.BooleanField(_('locked'), default=False)
    modified_count = models.SmallIntegerField(_('modified count'), default=0)

    class Meta:
        abstract = True

    def get_sentinel_user(self):
        # admin user id
        return get_user_model().objects.get(username='Admin')

    def save(self, modification=True, *args, **kwargs):
        # see if I can add created by and modified by here
        if self.id and modification:
            self.modified_count += 1
        return super(BaseModel, self).save(*args, **kwargs)