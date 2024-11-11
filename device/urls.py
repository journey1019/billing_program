from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceList, DeviceCreate, DeviceViewSet

app_name = 'device'

router = DefaultRouter()
router.register(r'device_data', DeviceViewSet, basename="device")

urlpatterns = [
    path('', DeviceList, name='device_list'),
    path('create/', DeviceCreate, name='device_create'),

    path("api/", include(router.urls)),
]
