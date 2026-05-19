from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    director_name = models.CharField(max_length=255)
    publication_year = models.PositiveSmallIntegerField()
    synopsis = models.TextField()
    image = models.ImageField(upload_to='movie_images/', blank=True, null=True)

    def __str__(self):
        return self.title
