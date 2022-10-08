# from django.forms import ModelForm
from .models import Task
from django import forms
class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title', 'description', 'important']
        widgets={                                   # widgets en minusculas
            'title':forms.TextInput(attrs={'class': 'form-control my-2','placeholder':'titulo...'}),
            'description': forms.Textarea(attrs={'class':'form-control my-2', 'placeholder':'descripcion...'}),
            'important': forms.CheckboxInput(attrs={'class':'form-check-input my-2'})
        }