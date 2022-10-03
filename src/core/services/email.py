import json
import logging
import os

from rest_framework.response import Response
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class EmailService:

    def __init__(self, receiver_email: str):
        self.receiver_email = receiver_email
        self.subject = 'Sending with Twilio SendGrid is Fun'
        self.body = '<strong>and easy to do anywhere, even with Python</strong>'

    def send_sendgrid_email(self):
        message = Mail(
            from_email=os.environ.get('SENDER_EMAIL'),
            to_emails=self.receiver_email,
            subject=self.subject,
            html_content=self.body)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            logging.info(f"EmailService: {response.status_code}")
            return Response({}, status=response.status_code)
        except Exception as e:
            logging.error(json.loads(e.body.decode())['errors'][0]['message'], exc_info=True)
            return Response({'message': f"EmailService: {json.loads(e.body.decode())['errors'][0]['message']}"},
                            status=e.status_code)
