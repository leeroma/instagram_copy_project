from django import forms

from instagram_app.models import Publication


class PublicationForm(forms.ModelForm):
    profile_id = forms.IntegerField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Publication
        exclude = ['created_at', 'updated_at', 'profile', 'likes',]