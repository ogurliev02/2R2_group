from app import app
from app import mail
from flask_mail import Message
from threading import Thread

def async_mail(f):
    def wrapper(*args, **kwargs):
        t = Thread(target=f, args=args, kwargs=kwargs)
        t.start()
    return wrapper

@async_mail
def send_async_mail(msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, to_who, text_body="", html_body=""):
    msg = Message(subject=subject, sender=sender, recipients=to_who)
    msg.body = text_body
    msg.html = html_body
    send_async_mail(msg)