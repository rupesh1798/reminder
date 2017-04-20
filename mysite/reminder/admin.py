from django.contrib import admin
from reminder.models import UserProfile
from reminder.models import Reminder
# Register your models here.
admin.site.register(Reminder)
admin.site.register(UserProfile)
