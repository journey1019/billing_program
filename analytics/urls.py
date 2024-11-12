# urls.py
from django.urls import path
from .views import CdrDeviceView

urlpatterns = [
    path('api/cdr-device/', CdrDeviceView.as_view(), name='cdr_device_data')
]
