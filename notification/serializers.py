from rest_framework import serializers
from .models import Notification
from accounts.models import User


class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model=Notification
        fields='__all__'
        
