from django.urls import path
from . import views

app_name = 'uploads' # 네임스페이스 정의
urlpatterns = [
    path("upload-csv/", views.upload_csv, name="upload_csv"),
    path("cdr_table/", views.cdr_table, name="cdr_table"),
]