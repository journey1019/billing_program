from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['device_manage_id', 'acct_num', 'profile_id', 'serial_number', 'activated', 'deactivated', 'ppid', 'modal_name', 'internet_mail_id', 'alias', 'remarks']
        widgets = {
            'device_manage_id': forms.TextInput(attrs={'placeholder': '고객 관리 ID'}),
            'acct_num': forms.TextInput(attrs={'placeholder': '고객 ID'}),
            'profile_id': forms.NumberInput(attrs={'placeholder': '고객 번호'}),  # 수정된 부분
            'serial_number': forms.TextInput(attrs={'placeholder': '단말 번호'}),
            'activated': forms.DateInput(attrs={'placeholder': '시작 날짜', 'type': 'date'}),  # type="date" 추가
            'deactivated': forms.DateInput(attrs={'placeholder': '종료 날짜', 'type': 'date'}),  # type="date" 추가
            'ppid': forms.NumberInput(attrs={'placeholder': '가격 번호'}),  # 수정된 부분
            'modal_name': forms.TextInput(attrs={'placeholder': '모델 이름'}),
            'internet_mail_id': forms.TextInput(attrs={'placeholder': '고객 메일 주소'}),
            'alias': forms.TextInput(attrs={'placeholder': '고객 별명'}),
            'remarks': forms.TextInput(attrs={'placeholder': '비고'}),
        }


class DeviceUploadForm(forms.Form):
    csv_file = forms.FileField()