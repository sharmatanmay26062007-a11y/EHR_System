from django import forms

from doctors.models import DoctorProfile

from .models import Appointment


class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(
        queryset=DoctorProfile.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Appointment
        fields = ('doctor', 'date', 'time_slot', 'reason')
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time_slot': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 11:00 AM'}),
            'reason': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brief reason for visit'}),
        }