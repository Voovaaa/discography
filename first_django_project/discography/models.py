from django.db import models
from django.core.validators import MinLengthValidator


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=100,
                            validators=[MinLengthValidator(3, message="Name's len must be more than 2")])
    date_published = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="tracks")

    def __str__(self):
        return f"{self.name}, artist - {self.artist}"


class Comment(models.Model):
    text = models.CharField(max_length=1000,
                            validators=[MinLengthValidator(3, message="Comment's len must be more than 2")])
    date_published = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"id-{self.pk}, artist-{self.artist}"
