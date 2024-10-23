from django import forms
from django.forms import ModelForm
from .models import Application

class RegistrationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['name','student_id_no', 'year_of_graduation', 'profile_pic']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_graduation': forms.NumberInput(attrs={'class': 'form-control'}),
            'student_id_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

