from django import forms
from .models import Track, Artist, Comment


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
        fields = ["name", "date_published"]