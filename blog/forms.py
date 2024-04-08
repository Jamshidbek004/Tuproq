from django import forms
from .models import Royxat,Comment


class royxatForm(forms.ModelForm):
    class Meta:
        model = Royxat
        fields ='__all__'
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']