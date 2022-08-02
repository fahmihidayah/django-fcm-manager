from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('fcm_form', TemplateView.as_view(template_name='fcm_app/form.html'), name='fcm_form'),
]