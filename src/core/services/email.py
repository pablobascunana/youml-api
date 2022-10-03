import json
import logging
import os

from rest_framework.response import Response
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class EmailService:

    @staticmethod
    def send_sendgrid_email(receiver_email: str, subject: str, body: str) -> Response:
        message = Mail(
            from_email=os.environ.get('SENDER_EMAIL'),
            to_emails=receiver_email,
            subject=subject,
            html_content=body)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            logging.info(f"EmailService: {response.status_code}")
            return Response({}, status=response.status_code)
        except Exception as e:
            logging.error(json.loads(e.body.decode())['errors'][0]['message'], exc_info=True)
            return Response({'message': f"EmailService: {json.loads(e.body.decode())['errors'][0]['message']}"},
                            status=e.status_code)
