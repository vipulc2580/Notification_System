from django.urls import path,include 
from notification.views import NotificationView
urlpatterns=[
    path('notifications/',NotificationView.as_view(),name='Notification'),
    path('users/<int:id>/notifications/',NotificationView.as_view(),name='User_Notification'),
]