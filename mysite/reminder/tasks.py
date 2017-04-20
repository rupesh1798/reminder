from django.conf import settings
from twilio.rest import Client
from reminder.models import Reminder
#import datetime, time
from datetime import datetime
from threading import Timer
account_sid = "ACa6d4cb06b269945f34462a435110511f"
auth_token = "4c74480dcf8daab2fc8a078e5ca40d43"
client = Client(account_sid, auth_token)

def send_sms_reminder(time):
    try:
        reminder = Reminder.objects.get(time__exact = time)

        print(reminder)
    except Reminder.DoesNotExist:
        return
    global body
    body = 'Hello!  '+ reminder.name + '. Your reminder is ' + reminder.message
    #print(time)
    #t1 = datetime.now()
    #t2 = time
    #delta = t2 - t1
    #sec = delta.seconds

    t = Timer(60, message)
    t.start()
def message():
    message = client.messages.create(
        body= body ,
        to="+917610002521",
        from_="+13176224171",
    )
