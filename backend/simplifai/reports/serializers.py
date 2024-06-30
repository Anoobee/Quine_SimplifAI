from rest_framework import serializers
from rest_framework import routers, serializers, viewsets
from .models import Chats, Report

class ChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chats
        fields = "__all__"

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"