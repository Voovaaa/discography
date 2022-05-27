from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=100)
    date_published = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name}, artist - {self.artist}"