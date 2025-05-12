from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):
    # create a user
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have a username')
        
        user=self.model(
            email=self.normalize_email(email), #normalized means lowercase the email
            username=username,
            first_name=first_name.strip(),
            last_name=last_name.strip()
        )
        user.set_password(password)
        #using parameter is used to define the db to be used
        user.save(using=self._db)
        return user

    # creater a superuser
    def create_superuser(self,first_name,last_name,username,email,password):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin= True
        user.is_active=True 
        user.is_staff=True 
        user.is_superadmin=True 
        user.save(using=self._db)
        return user
    
    
class User(AbstractBaseUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=12,blank=True)
    
    #required fields by django user model
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']

    objects=UserManager()
    
    class Meta:
        verbose_name='user'
        verbose_name_plural='users'

    def __str__(self):
        return self.email

    def has_perm(self,prem,obj=None):
        return self.is_admin 

    def has_module_perms(self,app_label):
        return True 
