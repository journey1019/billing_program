from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cdr.views import CDRViewSet
from networkreport.views import NRViewSet
from account.views import AccountViewSet
from device.views import DeviceViewSet
from pplan.views import PplanViewSet

router = DefaultRouter()
router.register(r'cdr', CDRViewSet, basename='cdr')
router.register(r'nr', NRViewSet, basename='nr')
router.register(r'account', AccountViewSet, basename='account')
router.register(r'device', DeviceViewSet, basename='device')
router.register(r'pplan', PplanViewSet, basename='pplan')

urlpatterns = [
    path('', include(router.urls)),
]
