import os

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

auth_token = os.getenv('TWILIO_AUTH_TOKEN')
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
my_number = os.getenv('MY_NUMBER')

client = Client(account_sid, auth_token)

body = 'Test message'
to = '+79130073119'

message = client.messages.create(
                              body=body,
                              from_=my_number,
                              to=to
                          )

print(message.sid)
