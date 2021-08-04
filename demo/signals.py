from django.db.models.signals import post_save
from django.core.signals import request_finished, request_started
from django.dispatch import receiver
from .consumers import WSConsumer

from .models import User
from .views import IndexPage

@receiver(post_save, sender=User)
def create_user_profile(sender, instance , created = False, **kwargs):
    print("worked")
    if created:
        # User.objects.create(user=instance)
        print(instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


@receiver(request_started, sender = IndexPage)
def my_callback(sender, **kwargs):
    print("Request finished!")