from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cdr.views import CDRViewSet
from networkreport.views import NRViewSet
from account.views import AccountViewSet

router = DefaultRouter()
router.register(r'cdr', CDRViewSet, basename='cdr')
router.register(r'nr', NRViewSet, basename='nr')
router.register(r'account', AccountViewSet, basename='account')

urlpatterns = [
    path('', include(router.urls)),
]
