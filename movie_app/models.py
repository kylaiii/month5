from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=True)
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.author.username + ' ' + self.text + ' ' + self.movie.title if self.author is not None else 'someone'