"""
Email Sender class to send emails
"""
from email.message import EmailMessage
import imghdr
import smtplib


class EmailSender:

    def __init__(self,
                 my_email: str,
                 my_password: str,
                 server: str = 'smtp.gmail.com',
                 port: int = 465):
        self.my_email = my_email
        self.my_password = my_password
        self.server = server
        self.port = port

    def send(self,
             subject: str,
             body: str,
             recipient: str,
             attachment_path: str = None):
        """
        Sends email
        """
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = body
        msg['To'] = recipient
        msg.set_content(body)

        # attach file
        if attachment_path:
            with open(attachment_path, 'rb') as f:
                file_data = f.read()
                file_name = f.name

            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

        with smtplib.SMTP_SSL(self.server, self.port) as smtp:
            smtp.login(self.my_email, self.my_password)
            smtp.send_message(msg)
