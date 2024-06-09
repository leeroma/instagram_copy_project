from django import forms
from django.forms import TextInput

from instagram_app.models import Publication


class PublicationForm(forms.ModelForm):
    user_id = forms.IntegerField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Publication
        exclude = ['created_at', 'updated_at', 'user', 'likes', ]


class SearchForm(forms.Form):
    search = forms.CharField(widget=TextInput(attrs={'class': 'search-input', 'placeholder': 'Search...', }),
                             label='', )
