from django import forms
from reminder.models import UserProfile
from django.contrib.auth.models import User

class ReminderForm(forms.Form):
    name = forms.CharField(max_length=150)
    phone_number = forms.CharField(max_length=15)
    message = forms.CharField(max_length=150)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('firstname','lastname','account_sid','auth_token','user_phone_number','twilio_phone_number')
