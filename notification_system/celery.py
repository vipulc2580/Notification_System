import os
from celery import Celery
from django.conf import settings 


os.environ.setdefault('DJANGO_SETTINGS_MODULE','notification_system.settings')

app=Celery('notification_system')
app.conf.enable=utc=False
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings,namespace='CELERY')


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    printf('Request :{self.request!r}')