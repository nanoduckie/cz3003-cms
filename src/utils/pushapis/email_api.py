"""
    Email API
"""
from django.core.mail import send_mail
from django.core.mail import EmailMessage


class EmailAPI:

    def push_update(self, to_email, subject, content, attachment=None):
        try:
            email = EmailMessage(
                subject, content, 'hungph2202@gmail.com', [to_email])
            if attachment:
                email.attach_file(attachment)
            email.send()
            return True
        except Exception as e:
            print(e)
            return False
