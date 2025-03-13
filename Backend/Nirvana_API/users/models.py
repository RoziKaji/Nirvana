from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from datetime import date
from django.core.validators import RegexValidator
# Create your models here.

class CustomUserManager(BaseUserManager):

    def _create_user(self, phone_number, password, username, **extrafields):
        if not phone_number:
            raise ValueError(" Phone number is invalid! ")
        User = self.model(phone_number = phone_number, username = username, **extrafields)
        User.set_password(password)
        User.save()
        return User
    
    def create_user(self, phone_number = None, password = None, username = None, **extrafields):
        extrafields.setdefault("is_staff" , False)
        extrafields.setdefault("is_superuser", False)
        return self._create_user(phone_number, password, username, **extrafields)

    def create_superuser(self, phone_number = None, password = None, username = None, **extrafields):
        extrafields.setdefault("is_staff" , True)
        extrafields.setdefault("is_superuser", True)
        return self._create_user(phone_number, password, username, **extrafields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, primary_key=False, blank=True, null=True)
    username = models.CharField(max_length=28, primary_key=False)
    phone_number = models.CharField(max_length=11, primary_key=False, unique=True, validators=[RegexValidator("09\d\d\d\d\d\d\d\d\d")])
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at= models.DateField(default= date.today)
    last_login =models.DateField(default=date.today)
    is_subscribed = models.BooleanField(default=False)
    subscribed_at = models.DateField(blank=True, null=True)
    subscription_end = models.DateField(blank=True, null=True)
    minutes_listened =models.IntegerField(default=0)
    objects = CustomUserManager()
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["username"]
    def __str__(self):
        return self.username