# Generated by Django 5.0.6 on 2024-06-20 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_alter_chats_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chats',
            name='chat_id',
        ),
    ]
