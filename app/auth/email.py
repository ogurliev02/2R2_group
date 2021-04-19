from flask import render_template
from app.email import send_email

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('Восстановление пароля в приложении Flask',
            sender=app.config['ADMINS'][0],
            to_who=[user.email],
            text_body=render_template('email/reset_password.txt', user=user, token=token),
            html_body=render_template('email/reset_password.html', user=user, token=token))