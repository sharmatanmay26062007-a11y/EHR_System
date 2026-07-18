from django import forms


class SymptomForm(forms.Form):
    symptoms = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Describe your symptoms, e.g. "fever and headache since 2 days"'
        }),
        label='What symptoms are you experiencing?'
    )