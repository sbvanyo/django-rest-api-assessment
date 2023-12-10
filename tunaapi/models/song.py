from django.db import models
from .artist import Artist

class Song(models.Model):

    title = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    length = models.IntegerField(null=True)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
