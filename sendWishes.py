from fbchat import Client
from fbchat.models import *
from icalendar import Calendar
import json
from datetime import date
u_name='<email or phone>'
p_word='<password>'
client=Client(u_name,p_word)
today = date.today()
file = open('birthday.ics', 'rb')
calendar = Calendar.from_ical(file.read())
entries = [dict(uid=event['UID'],summary=event['summary'])
           for event in calendar.walk('VEVENT')
           if event['DTSTART'].dt == today ]
for x in json.loads((json.dumps(entries, indent=2, sort_keys=True))):
    print(x['summary'])
    client.sendMessage('Happy Birthday',int(x['uid'][1:-13]),ThreadType.USER)
    
client.logout()
