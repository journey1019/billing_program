from django import forms
from .models import Pplan

class PplanForm(forms.ModelForm):
    class Meta:
        model = Pplan
        fields = ['ppid', 'basic_fee', 'subscription_fee', 'free_byte', 'surcharge_unit', 'each_surcharge_fee', 'apply_company', 'remarks', 'note']
        widgets = {
            'ppid': forms.NumberInput(attrs={'placeholder': 'PPID'}),
            'basic_fee': forms.NumberInput(attrs={'placeholder': 'Basic Fee'}),
            'subscription_fee': forms.NumberInput(attrs={'placeholder': 'Subscription Fee'}),
            'free_byte': forms.NumberInput(attrs={'placeholder': 'Free Byte'}),
            'surcharge_unit': forms.NumberInput(attrs={'placeholder': 'Surcharge Unit'}),
            'each_surcharge_fee': forms.NumberInput(attrs={'placeholder': 'Each Surcharge Fee'}),
            'apply_company': forms.TextInput(attrs={'placeholder': 'Apply Company'}),
            'remarks': forms.TextInput(attrs={'placeholder': 'Remarks'}),
            'note': forms.TextInput(attrs={'placeholder': 'Note'}),
        }