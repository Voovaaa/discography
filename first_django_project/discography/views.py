from django.shortcuts import render
from django.views import generic
from .models import Artist, Track
from .forms import TrackForm


class IndexView(generic.ListView):
    context_object_name = 'artists'
    template_name = 'discography/index.html'
    model = Artist


class ArtistDetailView(generic.DetailView):
    template_name = 'discography/artist_detail.html'
    model = Artist


class TrackCreateView(generic.CreateView):
    model = Track
    template_name = "discography/new_track.html"
    form_class = TrackForm
    success_url = "/"