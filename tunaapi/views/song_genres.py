"""View module for handling requests about song genres"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song, Genre, SongGenre


class SongGenreView(ViewSet):
    """Tuna api song genre view"""
    def retrieve(self, request, pk):
      """Handle GET requests for single song genres
      Returns:
          Response -- JSON serialized song genre
      """
      try:
          song_genre = SongGenre.objects.get(pk=pk)
          serializer = SongGenreSerializer(song_genre)
          return Response(serializer.data)
      except SongGenre.DoesNotExist as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
        
    def list(self, request):
      """Handle GET requests to get all song genres
      Returns:
          Response -- JSON serialized list of song_genres
      """
      song_genres = SongGenre.objects.all()   
      serializer = SongGenreSerializer(song_genres, many=True)
      return Response(serializer.data)
    
    
    def create(self, request):
      """Handle POST operations for song_genres
      Returns
          Response -- JSON serialized song_genre instance
      """
      song_id = Song.objects.get(pk=request.data["songId"])
      genre_id = Genre.objects.get(pk=request.data["genreId"])
      song_genre = SongGenre.objects.create(
          song_id=song_id,
          genre_id=genre_id
      )
      serializer = SongGenreSerializer(song_genre)
      return Response(serializer.data, status=status.HTTP_201_CREATED)

class SongGenreSerializer(serializers.ModelSerializer):
  """JSON serializer for song_genres"""

  class Meta:
      model = SongGenre
      fields = ('id', 'song_id', 'genre_id')
      depth = 1
