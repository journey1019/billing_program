from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceList, DeviceCreate, DeviceViewSet, DeviceUpload, DeviceRecentViewSet

app_name = 'device'

router = DefaultRouter()
router.register(r'device_data', DeviceViewSet, basename="device")
router.register(r'device-recent', DeviceRecentViewSet, basename='device-recent')


urlpatterns = [
    path('', DeviceList, name='device_list'),
    path('create/', DeviceCreate, name='device_create'),
    path('upload/', DeviceUpload, name='device_upload'),

    path("api/", include(router.urls)),
]
