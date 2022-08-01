from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User
from string import ascii_lowercase
from random import choices


def validate_date_published(value):
    if value > timezone.now().date():
        raise ValidationError(f"Date published must be > {timezone.now().date()}")


def generate_random_username():
    return choices(ascii_lowercase, 40)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, username=None):
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, username):
        user = self.create_user(email, password, username=username)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=40, blank=True, unique=True, null=True)
    email = models.EmailField(unique=True)
    objects = CustomUserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        if self.username:
            return f"{self.email}, {self.username}"
        else:
            return self.email


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


