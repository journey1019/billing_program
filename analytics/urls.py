# urls.py
from django.urls import path
from .views import CdrDeviceView

urlpatterns = [
    path('api/cdr-device/', CdrDeviceView.as_view(), name='cdr_device_data') # http://127.0.0.1:8000/analytics/api/cdr-device/?date_index=202409&serial_number=02121490SKY1197
]
