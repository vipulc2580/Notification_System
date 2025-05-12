from celery import shared_task
from .models import Notification
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from accounts.models import User
from twilio.rest import Client
import logging


logger = logging.getLogger('notification') 
# from django.core.mail import send_mail
@shared_task(bind=True, max_retries=3, default_retry_delay=60) 
def send_email_notification(self,notification_id):
    try:
        notification = Notification.objects.get(id=notification_id)
       
        from_email = settings.DEFAULT_FROM_EMAIL
        
        context={
            'message':notification.message,
        }
        message = render_to_string('emails/notification.html', context)
        to_email = notification.user.email
        mail = EmailMessage(notification.title, message, from_email, to=[to_email])
        mail.content_subtype = "html"  # Ensures email is sent as HTML
        mail.send()
        notification.status='sent'
        notification.save()
        # print('Email has been sent')
        logger.info(f"[EMAIL] Notification {notification.id} sent to {to_email}")
    except Exception as e:
        logger.error(f"[EMAIL] Failed to send notification {notification_id}: {e}")
        raise self.retry(exc=e)

@shared_task(bind=True, max_retries=3, default_retry_delay=60) 
def send_sms_notification(self,notification_id):
    # similar logic for SMS
    try:
        notification = Notification.objects.get(id=notification_id)
        ## i will send the email 
        print('notification found')
        account_sid=settings.TWILIO_ACCOUNT_SID
        auth_token=settings.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)
        print('connected to Twilio client')

        message = client.messages.create(
            body=f"Hi {notification.user.first_name},\n{notification.message}",
            from_=settings.TWILIO_PHONE_NUMBER,  # Example: '+12054403333'
            to=f"+91{notification.user.phone_number}"
        )
        print(message.sid)
        # print(verification.status)
        print('sms will has been sent')
        notification.status = "sent"
        notification.save()
        logger.info(f"[SMS] Message SID: {message.sid}")
    except Exception as e:
        logger.error(f"[SMS] Failed to send SMS for notification {notification_id}: {e}")
        raise self.retry(exc=e)
    
        
@shared_task(bind=True, max_retries=3, default_retry_delay=60) 
def send_in_app_notification(self,notification_id):
    # maybe save it to a redis/pubsub/websocket layer
    try:
        notification = Notification.objects.get(id=notification_id)
        print('in app notification has been sent')
        notification.status = "sent"
        notification.save()
        logger.info(f"[IN-APP] Notification {notification.id} marked as sent.")
    except Exception as e:
        logger.error(f"[IN-APP] Failed to send in-app notification {notification_id}: {e}")
        raise self.retry(exc=e)
