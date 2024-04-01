import os
import smtplib
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def send_sms(to: str, body: str):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    
    message = client.messages \
        .create(
            body=body,
            from_=os.getenv('TWILIO_PHONE_NUMBER'),
            to=to
        )
    
    return message.sid

def send_email(to: str, subject: str, body: str):
    sender = os.getenv('SMTP_USER')
    password = os.getenv('SMTP_PASS')
    smtp_server = os.getenv('SMTP_HOST')
    smtp_port = os.getenv('SMTP_PORT')

    text = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, to, text)
