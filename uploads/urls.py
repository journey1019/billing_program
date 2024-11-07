from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import upload_csv, cdr_table, CDRViewSet

app_name = 'uploads' # 네임스페이스 정의

router = DefaultRouter()
router.register(r'cdr_data', CDRViewSet, basename='cdr')  # API 엔드포인트를 'cdr_data'로 설정

urlpatterns = [
    path("upload-csv/", upload_csv, name="upload_csv"),
    path("cdr_table/", cdr_table, name="cdr_table"),
    path("api/", include(router.urls)), # API 엔드포인트를 포함
]