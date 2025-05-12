from django.contrib import admin
from .models import Notification
# Register your models here.
@admin.register(Notification)
class CustomNotificationAdmin(admin.ModelAdmin):
    list_display=['user','notification_type','status','created_at']
    ordering=('-created_at',)
    
