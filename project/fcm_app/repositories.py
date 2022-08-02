from .models import FcmApp, Device, Notification, models
from pyfcm import FCMNotification


class FcmAppRepository:

    def __init__(self):
        self.manager: models.Manager = FcmApp.objects
        self.default_query_set = self.manager.prefetch_related('device_set')

    def get_by_id(self, id: int) -> FcmApp:
        return self.default_query_set.get(models.Q(pk=id))

    def find_all(self):
        return self.default_query_set.all()

    def get_list_token(self, fcm_app: FcmApp) -> list:
        device_item: Device
        return list(device_item.token for device_item in fcm_app.device_set.all())

    def send_notification(self, fcm_id, notification: Notification):
        fcm_app: FcmApp = self.get_by_id(fcm_id)
        set_token = self.get_list_token(fcm_app=fcm_app)
        push_service: FCMNotification = FCMNotification(fcm_app.server_key)
        data_message = notification.get_additional_data()

        result = push_service.notify_multiple_devices(registration_ids=set_token,
                                                      message_title=notification.title,
                                                      message_body=notification.message,
                                                      data_message=data_message)
        print(result)


class DeviceRepository:

    def __init__(self):
        self.manager: models.Manager = Device.objects
        self.default_query_set = self.manager
