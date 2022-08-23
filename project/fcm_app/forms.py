from django.forms import ModelForm
from . import models


class DeviceForm(ModelForm):

    class Meta:
        model = models.Device
        fields = ['user_name', 'token', 'fcm_app']


class FcmAppForm(ModelForm):

    class Meta:
        model = models.FcmApp
        fields = ['name', 'server_key', 'sender_id']


class Notification(ModelForm):

    class Meta:
        model = models.Notification
        fields = ['fcm_app', 'title', 'message', 'link_url', 'image_url', 'action_url', 'additional_message']