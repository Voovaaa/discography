from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name = "discography"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ArtistDetailView.as_view(), name='artist_detail'),
    path('<int:pk>/new_track/', views.TrackCreateView.as_view(), name='new_track'),
    path('new_artist/', views.ArtistCreateView.as_view(), name='new_artist'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="discography:index"), name="logout")
]
