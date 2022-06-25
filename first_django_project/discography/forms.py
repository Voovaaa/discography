from django import forms
from django.contrib.auth import forms as auth_forms
from .models import Track, Artist, Comment, CustomUser


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


class CustomUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["email"]