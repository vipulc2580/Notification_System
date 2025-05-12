from django.shortcuts import render
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 
from accounts.models import User
from .tasks import send_email_notification,send_sms_notification,send_in_app_notification
# Create your views here.


class NotificationView(APIView):
    def post(self,request):
        serializer=NotificationSerializer(data=request.data)
        if serializer.is_valid():
            # print(serializer.data)
            notification_instance=serializer.save()
            if notification_instance.notification_type=='email':
                send_email_notification(notification_instance.id)
            elif notification_instance.notification_type=='sms':
                send_sms_notification(notification_instance.id)
            elif notification_instance.notification_type=='in_app':
                send_in_app_notification(notification_instance.id)
            return Response({'message':'Notification is saved and will be sent'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'Will respond you soon'},status=status.HTTP_400_BAD_REQUEST)    
            

    def get(self,request,id):
        try:
            user=User.objects.get(pk=id)
        except User.DoesNotExist:
            return Response({'message':'Invalid User Id'},status=status.HTTP_400_BAD_REQUEST)
        user_notifications=Notification.objects.filter(user=user)
        serializer=NotificationSerializer(user_notifications,many=True)
        return Response({'data':serializer.data},status=status.HTTP_200_OK)
