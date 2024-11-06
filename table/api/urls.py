from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CdrViewSet, NetworkReportViewSet, AccountViewSet, DeviceManageViewSet, PricePlanViewSet

router = DefaultRouter()
router.register(r'cdr', CdrViewSet)
router.register(r'networkreport', NetworkReportViewSet)
router.register(r'account', AccountViewSet)
router.register(r'device', DeviceManageViewSet)  # 이름 변경
router.register(r'pplan', PricePlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
