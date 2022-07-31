from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import GalleryImage, Project


@receiver(post_delete, sender=Project)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.image.delete(save=False)


@receiver(post_delete, sender=GalleryImage)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.image.delete(save=False)
