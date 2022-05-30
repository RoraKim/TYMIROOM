from msilib.schema import Property
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta, timezone
from django.conf import settings


# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    
class GuestBook(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    me = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='guestbook_me')
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='guestbook_friend')
    
    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at
        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.registered_date.date()
            return str(time.days) + '일 전'
        else:
            return self.created_at.date

class Profile(models.Model):
    tymi_image = models.CharField(max_length=20, default="pink")
    room_image = models.CharField(max_length=20, default="1")
    level = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    life_movie = models.CharField(max_length=100, default="", null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)