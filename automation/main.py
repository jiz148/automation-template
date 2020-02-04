"""
Main.py
"""
import os

from common.downloader import Downloader
from common.email_sender import EmailSender
from common.modifier import Modifier


def run():
    # Download data

    test_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cat.jpg')
    downloader = Downloader('https://www.wfmt.com/wp-content/uploads/2019/07/kitten-cat-piano-mammal-fauna-pets-645664-pxhere.com_.jpg', test_path)
    downloader.download()

    # Modify data

    modifier = Modifier()
    modifier.modify()

    # Send email

    my_email = ''
    my_password = ''
    email_sender = EmailSender(my_email, my_password)
    subject = ''
    body = ''
    recipient = ''
    email_sender.send(subject, body, recipient, test_path)


if __name__ == "__main__":
    run()
