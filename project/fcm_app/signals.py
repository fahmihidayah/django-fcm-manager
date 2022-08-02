from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FcmApp, Notification, Device, models

from .repositories import FcmAppRepository


@receiver(post_save, sender=Notification)
def send_notifications(sender : Notification, **kwargs):
    fcm_repository: FcmAppRepository = FcmAppRepository()
    notification: Notification = kwargs['instance']
    fcm_repository.send_notification(notification.fcm_app.pk, notification)

