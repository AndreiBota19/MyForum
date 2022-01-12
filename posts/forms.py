from django import forms
from django.forms import widgets
from .models import Comment



class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
        