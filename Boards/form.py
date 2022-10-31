from dataclasses import field
from statistics import mode
from django import forms
from .models import *

class NewBoardForm(forms.ModelForm):
    class Meta:
        model = BoardData
        fields = ['name', 'description']

class NewTopicForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(
        attrs={'rows':5, 'placeholder':'Enter your content here'}
    ), max_length=4000, help_text='The max length is 4000')
    class Meta:
        model = TopicData
        fields = ['title', 'content']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = PostData
        fields = ['content', ]