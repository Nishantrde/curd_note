from notepad import settings
from django.core.mail import send_mail

def send_email_token(email, token):
    try:
        subject = "Your account is verified"
        message = f"Click on the link to verify https://curd-note.vercel.app//notepad/verify/{token}"
        email_form = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_form, recipient_list)
    except Exception as e:
        print("error", e)
        return False
    return True