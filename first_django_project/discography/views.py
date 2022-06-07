from django.shortcuts import redirect
from django.views import generic
from .models import Artist, Track
from .forms import TrackForm, ArtistForm, CommentForm


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
        comment.artist_id = self.kwargs['pk']
        comment.save()
        return redirect('discography:artist_detail', pk=self.kwargs['pk'])


class TrackCreateView(generic.CreateView):
    model = Track
    template_name = "discography/new_track.html"
    form_class = TrackForm
    success_url = "/"


class ArtistCreateView(generic.CreateView):
    model = Artist
    template_name = "discography/new_artist.html"
    form_class = ArtistForm
    success_url = "/"