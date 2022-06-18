from django.shortcuts import redirect
from django.views import generic
from .models import Artist, Track
from .forms import TrackForm, ArtistForm, CommentForm
from django.urls import reverse, reverse_lazy


class IndexView(generic.ListView):
    context_object_name = 'artists'
    template_name = 'discography/index.html'
    model = Artist


class ArtistDetailView(generic.CreateView, generic.DetailView):
    template_name = 'discography/artist_detail.html'
    model = Artist
    form_class = CommentForm


    def form_valid(self, form):
        comment = form.save(commit=False)
        pk = self.kwargs['pk']
        comment.artist_id = pk  # PRIMARY KEY = ID
        comment.save()
        return redirect('discography:artist_detail', pk=self.kwargs['pk'])


class TrackCreateView(generic.CreateView):
    model = Track
    template_name = "discography/new_track.html"
    form_class = TrackForm

    def form_valid(self, form):
        track = form.save(commit=False)
        artist_pk = self.kwargs['pk']
        track.artist_id = artist_pk
        track.save()
        return redirect("discography:artist_detail", pk=track.artist_id)


class ArtistCreateView(generic.CreateView):
    model = Artist
    template_name = "discography/new_artist.html"
    form_class = ArtistForm
    success_url = reverse_lazy("discography:index")