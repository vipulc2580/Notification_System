from celery import shared_task
from .models import Notification
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from accounts.models import User
from twilio.rest import Client

# from django.core.mail import send_mail

@shared_task(bind=True)
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
        print('Email has been sent')
    except Exception as e:
        print(e)

@shared_task(bind=True)
def send_sms_notification(self,notification_id):
    # similar logic for SMS
    
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
    
        

@shared_task(bind=True)
def send_in_app_notification(self,notification_id):
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
