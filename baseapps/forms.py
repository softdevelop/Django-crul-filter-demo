from django import forms
from django.forms import ModelForm
from .models import *

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name', 'sex', 'age',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter name...'}),    
            'sex': forms.Select(attrs={'class': 'form-control',}),    
            'age': forms.NumberInput(attrs={'class': 'form-control','placeholder':'Enter age...'}),            
        }
