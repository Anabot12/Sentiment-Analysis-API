from django import forms
from .models import SentimentModel
from django.http import JsonResponse

class SentimentForm(forms.ModelForm):
    comment = forms.CharField(max_length=500, widget=forms.TextInput(
        attrs={
            'class': 'comment',
            'placeholder': 'Enter your comment',
        }
    ))

    class Meta:
        model = SentimentModel
        fields = ['comment']