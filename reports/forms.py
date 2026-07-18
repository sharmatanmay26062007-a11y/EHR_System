from django import forms

from .models import LabReport


class LabReportForm(forms.ModelForm):
    class Meta:
        model = LabReport
        fields = ('report_type', 'file')
        widgets = {
            'report_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Blood Test, X-Ray'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }