from django import forms
from django.core.exceptions import ValidationError
from .models import Track, Artist, Comment
from django.utils import timezone


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ["name"]


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ["name", "date_published", "artist"]


    def clean_date_published(self):
        if self.cleaned_data['date_published'] > timezone.now().date():
            raise ValidationError("Invalid date: track can't be published in future")
        return self.cleaned_data['date_published']
    