from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cdr.views import CDRViewSet
from networkreport.views import NRViewSet

router = DefaultRouter()
router.register(r'cdr', CDRViewSet, basename='cdr')
router.register(r'nr', NRViewSet, basename='nr')

urlpatterns = [
    path('', include(router.urls)),
]
