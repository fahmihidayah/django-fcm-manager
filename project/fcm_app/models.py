from django.db import models

# Create your models here.


class FcmApp(models.Model):

    name: models.CharField = models.CharField(max_length=255)

    server_key: models.CharField = models.CharField(max_length=2000)

    sender_id: models.CharField = models.CharField(max_length=1000)

    created_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    updated_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Device(models.Model):

    user_name: models.CharField = models.CharField(max_length=255, default='')

    token: models.TextField = models.TextField(max_length=2000, default='')

    fcm_app: models.ForeignKey = models.ForeignKey(to=FcmApp, on_delete=models.CASCADE)

    created_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    updated_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name


class Notification(models.Model):

    title: models.CharField = models.CharField(max_length=2000, default='')

    message: models.TextField = models.TextField(max_length=2000, default='')

    link_url: models.CharField = models.CharField(max_length=2000, default='', null=True, blank=True)

    image_url: models.CharField = models.CharField(max_length=2000, default='', null=True, blank=True)

    action_url: models.CharField = models.CharField(max_length=2000, default='', null=True, blank=True)

    additional_message: models.TextField = models.TextField(max_length=3000, default='', null=True, blank=True)

    fcm_app: models.ForeignKey = models.ForeignKey(to=FcmApp, on_delete=models.CASCADE)

    created_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    updated_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    def get_additional_data(self):
        additional_data = {
            'msg': self.message,
            'contentTitle': self.title,
        }
        if self.link_url:
            additional_data['openurl'] = self.link_url

        if self.image_url:
            additional_data['openimage'] = self.image_url

        if self.action_url:
            additional_data['action_url'] = self.action_url

        return additional_data

    def __str__(self):
        return self.title