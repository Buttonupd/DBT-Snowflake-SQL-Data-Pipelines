from django import forms
from django.forms import ModelForm

from .models import Sentiment,Movie

class SentimentForm(forms.ModelForm):
    class Meta:
        model = Sentiment

        help_text = {
            'reviews':'Enter a short movie review'
        }

        fields = [
            'reviews',
            'gender',
            'age',
            'country'
        ]

        def __init__(self) -> object:
            super(SentimentForm, self).__init__(*args, **kwargs)
            self.fields['movie'] = forms.ModelChoiceField(queryset=Movie.objects.all())
            self.fields['movie'].required = True
            