from django.urls import path
from . import views


app_name = "discography"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ArtistDetailView.as_view(), name='artist_detail'),
    path('<int:pk>/new_track/', views.TrackCreateView.as_view(), name='new_track'),
    path('new_artist/', views.ArtistCreateView.as_view(), name='new_artist')
]
