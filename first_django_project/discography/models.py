from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django.core.exceptions import ValidationError


def validate_date_published(value):
    if value > timezone.now().date():
        raise ValidationError(f"Date published must be > {timezone.now().date()}")


class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=100,
                            validators=[MinLengthValidator(3, message="Name's len must be more than 2")])
    date_published = models.DateField(validators=[validate_date_published])
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="tracks")

    def __str__(self):
        return f"{self.name}, artist - {self.artist}"

    class Meta:
        unique_together = ('name', 'artist')
        ordering = ['date_published']


class Comment(models.Model):
    text = models.CharField(max_length=1000,
                            validators=[MinLengthValidator(3, message="Comment's len must be more than 2")])
    date_published = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey("Comment", on_delete=models.CASCADE,
                                       related_name="children", blank=True, null=True)

    def __str__(self):
        return f"id-{self.pk}, artist-{self.artist}"

    class Meta:
        ordering = ['-date_published']
