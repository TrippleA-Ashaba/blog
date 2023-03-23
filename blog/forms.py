from django import forms
from django.forms import ModelForm

from blog.models import Comment


class CommentForm(ModelForm):
    name = forms.CharField(label="Name", min_length=5, max_length=25)
    content = forms.CharField(max_length=500)

    class Meta:
        model = Comment
        fields = ("name", "content")
