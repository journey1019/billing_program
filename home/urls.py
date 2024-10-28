from django.urls import path
from .views import home, upload_file, upload_network_report

urlpatterns = [
    path('', home, name='home'),
    path('upload/cdr/', upload_file, name='upload_file'),  # 'upload_file' 패턴 확인
    path('upload/network-report/', upload_network_report, name='upload_network_report'),  # Network Report 업로드 URL 추가
]