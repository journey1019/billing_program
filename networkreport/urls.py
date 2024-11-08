from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NetworkReportUploadCSV, NRTable, NRViewSet

app_name = 'nr' # 네임스페이스 정의

router = DefaultRouter()
router.register(r'nr_data', NRViewSet, basename='nr')  # API 엔드포인트를 'cdr_data'로 설정

urlpatterns = [
    path("upload-nr/", NetworkReportUploadCSV, name="upload_nr"),
    path("nr_table/", NRTable, name="nr_table"),
    path("api/", include(router.urls)), # API 엔드포인트를 포함
]