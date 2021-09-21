# imports for signals
from django.conf import settings
from django.core.mail import send_mail
import uuid
from .models import Profile
from django.db.models.signals import post_save
# import user model
from django.contrib.auth import get_user_model
User = get_user_model()

# signal


def user_profile(sender, instance, created, **kwargs):

    if created:
        token = uuid.uuid4()
        Profile.objects.create(
            user=instance,
            name=f'{instance.first_name} {instance.last_name}',
            email=instance.email,
            gender=instance.gender,
            token=token,
        )
        mailer(instance, token)


post_save.connect(user_profile, sender=User)

# sending verify link with mail


def mailer(user, token):
    subject = 'Verify your account'
    msg = f' Hellow {user.first_name} {user.last_name} to verify your account http://127.0.0.1:8000/accounts/{token}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject=subject, message=msg, from_email=from_email,
              recipient_list=recipient_list)
