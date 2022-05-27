from django.urls import path
from . import views


app_name = "discography"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ArtistDetailView.as_view(), name='artist_detail'),
]
