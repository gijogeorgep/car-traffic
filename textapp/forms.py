
from django import forms

from .models import Student

class studreg(forms.ModelForm):
    class Meta:
        model=Student
        # fields=[]
        fields="__all__"