# Generated by Django 3.0.3 on 2020-05-25 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200525_0308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='public identifier')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_locked', models.BooleanField(default=False, verbose_name='locked')),
                ('modified_count', models.SmallIntegerField(default=0, verbose_name='modified count')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='name')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chatrooms_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'chatroom',
                'verbose_name_plural': 'chatrooms',
            },
        ),
    ]
