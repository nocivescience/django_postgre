from logging import PlaceHolder
from tkinter import Widget
from django.forms import ModelForm
from .models import Task
from django import forms
class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title', 'description', 'important']
        widgets={                                   # widgets en minusculas
            'title':forms.TextInput(attrs={'class': 'form-control my-2','placeholder':'title...'}),
            'description': forms.Textarea(attrs={'class':'form-control my-2', 'placeholder':'description...'}),
            'important': forms.CheckboxInput(attrs={'class':'form-check-input my-2'})
        }