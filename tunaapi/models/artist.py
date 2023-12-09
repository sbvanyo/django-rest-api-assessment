from django.db import models

class Artist(models.Model):

    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    bio = models.CharField(max_length=500)
    song_count = models.IntegerField(null=True)
