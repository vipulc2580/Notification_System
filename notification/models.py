from django.db import models
from accounts.models import User 
# Create your models here.
class Notification(models.Model):
    NOTIF_TYPES = (('email', 'Email'), ('sms', 'SMS'), ('in_app', 'In-App'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_type = models.CharField(choices=NOTIF_TYPES, max_length=10)
    message = models.TextField()
    status = models.CharField(max_length=20, default='pending')  # pending/sent/failed
    created_at = models.DateTimeField(auto_now_add=True)
    seen=models.BooleanField(default=False)
    seen_at=models.DateTimeField(blank=True,null=True)
    
    
    def __str__(self):
        return f'{self.user},{self.message},{self.notification_type},'
    
