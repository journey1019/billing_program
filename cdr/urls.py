from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CDRUploadCSV, CDRTable, CDRViewSet, CDRSummaryViewSet, CDRSummaryCreateView

app_name = 'cdr' # 네임스페이스 정의

router = DefaultRouter()
router.register(r'cdr_data', CDRViewSet, basename='cdr')  # API 엔드포인트를 'cdr_data'로 설정
router.register(r'cdrsummary', CDRSummaryViewSet)

urlpatterns = [
    path("upload-csv/", CDRUploadCSV, name="upload_csv"),
    path("cdr_table/", CDRTable, name="cdr_table"),
    path('cdrsummary/create/', CDRSummaryCreateView.as_view(), name='cdr-summary-create'),  # POST 요청으로 데이터 삽입
    path("api/", include(router.urls)), # API 엔드포인트를 포함

]