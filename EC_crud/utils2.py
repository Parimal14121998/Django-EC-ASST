from django.conf import settings
from django.core.mail import send_mail

def send_BMI_email(email,bmi,dt):
    try:
        
        subject = "EC BMI Tool"
        message = f"Your BMI is {bmi} calculated on {dt}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list=[email,]
        send_mail(subject,message,email_from,recipient_list)
        return "Email Send successfully"
        
    except Exception as e:
        return "Something went wrong"



