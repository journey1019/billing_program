from django.urls import path, include

from .views import table
# from .views import (table, CDRListCreateAPIView, NetworkReportListCreateAPIView, AccountListCreateAPIView, DeviceListCreateAPIView, PricePlanListCreateAPIView)

urlpatterns = [
    path('table/', table, name='table'),

    # path('api/cdr/', CDRListCreateAPIView.as_view(), name='cdr-list-create'),
    # path('api/networkreport/', NetworkReportListCreateAPIView.as_view(), name='nr-list-create'),
    # path('api/account/', AccountListCreateAPIView.as_view(), name='account-list-create'),
    # path('api/device/', DeviceListCreateAPIView.as_view(), name='device-list-create'),
    # path('api/pplan/', PricePlanListCreateAPIView.as_view(), name='pplan-list-create'),

    path('api/', include('table.api.urls')), # API URL 추가
]