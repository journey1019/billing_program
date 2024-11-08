from django import forms
from .models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['acct_num', 'acct_name', 'acct_resident_num', 'classification', 'invoice_address', 'invoice_address2', 'invoice_postcode']
        widgets = {
            'classification': forms.TextInput(attrs={'placeholder': '고객 유형 입력'}),
            'invoice_address': forms.TextInput(attrs={'placeholder': '주소 입력'}),
            'invoice_address2': forms.TextInput(attrs={'placeholder': '상세 주소 입력'}),
            'invoice_postcode': forms.NumberInput(attrs={'placeholder': '우편번호 입력'}),
        }
