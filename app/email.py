from app import mail
from flask_mail import Message
from threading import Thread
from flask import current_app

def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, to_who, text_body="", html_body=""):
    msg = Message(subject=subject, sender=sender, recipients=to_who)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_mail,
            args=(current_app._get_current_object(), msg)).start()