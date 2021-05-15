import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
# from api.models import *

logger = logging.getLogger(__name__)

@receiver(post_save, sender=MainUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=MainUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    logger.debug(f'New profile created  with email : {instance}')
    logger.info(f'New profile created with email : {instance}')
