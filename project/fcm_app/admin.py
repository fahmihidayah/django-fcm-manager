from django.contrib import admin
from . import forms
from . import models
# Register your models here.


@admin.register(models.FcmApp)
class FcmAppDataAdmin(admin.ModelAdmin):

    form = forms.FcmAppForm
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']


@admin.register(models.Device)
class DeviceDataAdmin(admin.ModelAdmin):

    form = forms.DeviceForm
    list_display = ['user_name', 'token', 'fcm_app', 'created_at', 'updated_at']
    search_fields = ['user_name', 'token']


@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):

    form = forms.Notification
    list_display = ['title', 'message', 'fcm_app', 'created_at', 'updated_at']
    search_fields = ['title', 'message', 'fcm_app']

    def save_model(self, request, obj, form, change):
        super(NotificationAdmin, self).save_model(request, obj, form, change)