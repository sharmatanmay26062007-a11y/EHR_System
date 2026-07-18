from django import forms
from django.forms import inlineformset_factory

from .models import MedicalRecord, Prescription


class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ('diagnosis', 'notes')
        widgets = {
            'diagnosis': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Viral Fever'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Consultation notes...'}),
        }


PrescriptionFormSet = inlineformset_factory(
    MedicalRecord, Prescription,
    fields=('medicine_name', 'dosage', 'duration', 'instructions'),
    widgets={
        'medicine_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicine name'}),
        'dosage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '500mg'}),
        'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '5 days'}),
        'instructions': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'After meals'}),
    },
    extra=1, can_delete=True
)