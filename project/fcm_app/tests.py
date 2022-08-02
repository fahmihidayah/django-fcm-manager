from django.test import TestCase
from .models import FcmApp, Device, Notification, models
from .repositories import FcmAppRepository

# Create your tests here.


class RepositoryTestCase(TestCase):

    def setUp(self) -> None:
        self.fcm_repository: FcmAppRepository = FcmAppRepository()
        self.fcm_app: FcmApp = FcmApp.objects.create(name='test_fcm_app', server_key='1234', sender_id='1234')
        self.device: Device = Device.objects.create(user_name='fahmi', token='token_test', fcm_app=self.fcm_app)

    def test_fcm_query_size_1(self):
        self.assertEqual(1, self.fcm_repository.find_all().count())

    def test_get_fcm_data(self):
        fcm_data: FcmApp = self.fcm_repository.get_by_id(1)
        self.assertEqual('test_fcm_app', fcm_data.name)

    def test_get_list_token(self):
        fcm_data: FcmApp = self.fcm_repository.get_by_id(1)
        self.assertEqual(1, len(self.fcm_repository.get_list_token(fcm_app=fcm_data)))


class ModelTestCase(TestCase):

    def setUp(self) -> None:
        self.fcm_app: FcmApp = FcmApp.objects.create(name='test_fcm_app', server_key='server_key_test', sender_id='sender_id_test')
        self.device: Device = Device.objects.create(user_name='fahmi', token='token_test', fcm_app=self.fcm_app)

    def test_fcm_query_size_1(self):
        self.assertEqual(1, FcmApp.objects.all().count())

    def test_device_query_size_1(self):
        self.assertEqual(1, Device.objects.all().count())

    def test_device_query_from_fcm_app_size_1(self):
        fcm_data: FcmApp = FcmApp.objects.prefetch_related('device_set').get(models.Q(pk=self.fcm_app.pk))
        self.assertTrue(hasattr(fcm_data, 'device_set'))

    def test_device_query_from_fcm_name_fahmi_true(self):
        fcm_data: FcmApp = FcmApp.objects.prefetch_related('device_set').get(models.Q(pk=self.fcm_app.pk))
        device: Device
        for device in fcm_data.device_set.all():
            self.assertEqual('fahmi', device.user_name)
