# import logging
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import *
# # from api.models import *
#
# logger = logging.getLogger(__name__)
#
# @receiver(post_save, sender=Book)
# def book_created(sender, instance, created, **kwargs):
#     if created:
#         BookDetail.objects.create(book=instance)
#
# @receiver(post_save, sender=Book)
# def save_book_detail(sender, instance, **kwargs):
#     instance.book_detail.save()
#     logger.debug(f'Book detail created  : {instance}')
#     logger.info(f'Book detail created : {instance}')
