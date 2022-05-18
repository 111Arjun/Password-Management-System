from django import forms
from .models import SaveData

class DataForm(forms.ModelForm):
    class Meta:
        model = SaveData
        fields = ['website', 'username']