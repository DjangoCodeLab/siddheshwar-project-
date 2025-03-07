from twilio.rest import Client

account_sid = 'AC8447d46f100dc595c4ee30a247b05792'
auth_token = '3566c34d61ded89c14253c33425e45a6'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+919236383276'
)

print(message.sid)