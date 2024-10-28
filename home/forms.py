# 사용자가 CSV 파일을 업로드할 수 있는 폼
from django import forms

# CDR CSV 파일 업로드 폼
class CDRUploadForm(forms.Form):
    csv_file = forms.FileField(label='Select a CSV file')

# Network Report CSV 파일 업로드 폼
class NetworkReportUploadForm(forms.Form):
    csv_file = forms.FileField(label='Select a Network Report CSV file')
