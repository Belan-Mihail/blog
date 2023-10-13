from .models import Comment
from django import forms

# 55 import and add class
# 56 view

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)