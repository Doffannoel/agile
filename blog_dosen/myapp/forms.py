from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    birthdate = forms.DateField(
        required=False, 
        input_formats=['%Y-%m-%d', '%d/%m/%Y', '%m-%d-%Y'],
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Registration
        fields = ['name', 'gender', 'phone', 'email', 'birthdate', 'age', 'address', 'education', 'cv']


