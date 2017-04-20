from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Reminder(models.Model):
    name = models.CharField(max_length=150)
    time = models.DateTimeField()
    phone_number = models.CharField(max_length=15)
    message = models.CharField(max_length=150)
    #task_id = models.CharField(max_length=50, blank=True, editable=False)
    def __str__(self):
        return self.name
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    account_sid = models.CharField(max_length=40)
    auth_token = models.CharField(max_length=40)
    user_phone_number = models.CharField(max_length=15)
    twilio_phone_number = models.CharField(max_length=15)
    #picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
