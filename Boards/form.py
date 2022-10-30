from django import forms
from .models import *

class NewBoardForm(forms.ModelForm):
    class Meta:
        model = BoardData
        fields = ['name', 'description']