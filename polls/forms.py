### CSV 파일 업로드 및 데이터 삽입
from django import forms

# 사용자 CSV 파일 업로드
class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()
