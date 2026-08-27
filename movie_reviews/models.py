from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.IntegerField()
    description = models.TextField(max_length=700)

    def __str__(self):
        return self.title