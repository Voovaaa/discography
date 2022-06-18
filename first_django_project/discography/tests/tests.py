from django.test import TestCase
from django.urls import reverse
from ..models import Artist, Track
from http import HTTPStatus
import datetime as dt


class TestArtistDetailView(TestCase):
    def test_get(self):
        artist = Artist.objects.create(name="artist1")
        track1 = Track.objects.create(name="track1", date_published="0001-1-1", artist=artist)
        track2 = Track.objects.create(name="track2", date_published="0002-2-2", artist=artist)
        url = reverse("discography:artist_detail", args=[artist.pk])

        response = self.client.get(url)

        expected_tracks = set(response.context_data["artist"].tracks.all())
        actual_tracks = {track1, track2}

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "discography/artist_detail.html")
        self.assertEqual(expected_tracks, actual_tracks)


class TestIndexView(TestCase):
    def test_get(self):
        url = reverse("discography:index")
        artist1 = Artist.objects.create(name="artist1")
        artist2 = Artist.objects.create(name="artist2")

        response = self.client.get(url)

        expected_artists = list(Artist.objects.values_list("id", flat=True))
        actual_artists = list(response.context_data["artists"].values_list("id", flat=True))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "discography/index.html")
        self.assertEqual(actual_artists, expected_artists)


class TestArtistCreateView(TestCase):
    def test_create(self):
        url = reverse("discography:new_artist")

        artist_name = "Artist New"

        response = self.client.post(url, data={"name": artist_name})

        expected_success_url = reverse("discography:index")
        is_created = Artist.objects.filter(name=artist_name).exists()

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, expected_success_url)
        self.assertTrue(is_created)


class TestTrackCreateView(TestCase):
    def test_create(self):
        artist = Artist.objects.create(name="artist")
        name = "track"
        date_published = "0001-01-01"
        data = {"name": name, "date_published": date_published}

        url = reverse("discography:new_track", args=[artist.pk])

        response = self.client.post(url, data=data)

        expected_succes_url = reverse("discography:artist_detail", args=[artist.pk])
        track_exists = Track.objects.filter(name=name, date_published=date_published, artist=artist).exists()

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertTrue(track_exists)
        self.assertRedirects(response, expected_succes_url)