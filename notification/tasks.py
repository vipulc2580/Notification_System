# notifications/tasks.py
from celery import shared_task
from .models import Notification
# from django.core.mail import send_mail

@shared_task(bind=True, max_retries=3, default_retry_delay=5)
def send_email_notification(self, notification_id):
    try:
        notification = Notification.objects.get(id=notification_id)
        ## i will send the email 
        print('email has been sent')
        notification.status = "sent"
        notification.save()
    except Exception as e:
        notification.status = "failed"
        notification.save()
        raise self.retry(exc=e)

@shared_task(bind=True, max_retries=3, default_retry_delay=5)
def send_sms_notification(notification_id):
    # similar logic for SMS
    try:
        notification = Notification.objects.get(id=notification_id)
        ## i will send the email 
        print('sms will has been sent')
        notification.status = "sent"
        notification.save()
    except Exception as e:
        notification.status = "failed"
        notification.save()
        raise self.retry(exc=e)

@shared_task(bind=True, max_retries=3, default_retry_delay=5)
def send_in_app_notification(notification_id):
    # maybe save it to a redis/pubsub/websocket layer
    try:
        notification = Notification.objects.get(id=notification_id)
        ## i will send the email 
        print('in app notification has been sent')
        notification.status = "sent"
        notification.save()
    except Exception as e:
        notification.status = "failed"
        notification.save()
        raise self.retry(exc=e)
