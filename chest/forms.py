from django import forms
from django.forms import ModelForm
from chest.models import Toast

class ToastForm(ModelForm):
    class Meta:
        model   = Toast
        fields  = '__all__'
        widgets = {
            'tags': forms.CheckboxSelectMultiple,
        }