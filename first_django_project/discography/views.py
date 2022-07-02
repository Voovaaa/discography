from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic
from .models import Artist, Track, CustomUser
from .forms import TrackForm, ArtistForm, CommentForm, CustomUserForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import views as auth_views
from django.contrib.auth import login


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


class TrackCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy("discography:login")
    model = Track
    template_name = "discography/new_track.html"
    form_class = TrackForm

    def form_valid(self, form):
        track = form.save(commit=False)
        artist_pk = self.kwargs['pk']
        track.artist_id = artist_pk
        track.save()
        return redirect("discography:artist_detail", pk=track.artist_id)


class ArtistCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy("discography:login")
    model = Artist
    template_name = "discography/new_artist.html"
    form_class = ArtistForm
    success_url = reverse_lazy("discography:index")


class RegistrationView(generic.CreateView):
    model = CustomUser
    template_name = "discography/registration.html"
    form_class = CustomUserForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("discography:index")


class Login(auth_views.LoginView):
    template_name = "discography/login.html"

    def get_success_url(self):
        return reverse("discography:index")

