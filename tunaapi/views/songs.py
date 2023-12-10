"""View module for handling requests about songs"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song, Artist


class SongView(ViewSet):
    """Tuna api song view"""
    def retrieve(self, request, pk):
      """Handle GET requests for single song
      Returns:
          Response -- JSON serialized song
      """
      try:  
          song = Song.objects.get(pk=pk)
          serializer = AllInfoSongSerializer(song)
          return Response(serializer.data, status=status.HTTP_200_OK)
      except Song.DoesNotExist as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    
    def list(self, request):
      """Handle GET requests to get all songs
      Returns:
          Response -- JSON serialized list of songs
      """
      songs = Song.objects.all()
      
      # filter to query songs by artist_id
      artist = request.query_params.get('artist_id', None)
      if artist is not None:
          songs = songs.filter(artist_id_id=artist)
   
      # filter to query songs by genre_id
      requested_genre = request.query_params.get('genre_id', None)
      if requested_genre is not None:
          songs = Song.objects.filter(genres__genre_id__id=requested_genre)
        
      serializer = SongSerializer(songs, many=True)
      return Response(serializer.data)
    
    
    def create(self, request):
      """Handle POST operations for songs
      Returns 
          Response -- JSON serialized song instance
      """
      artist_id = Artist.objects.get(pk=request.data["artist_id"])
      song = Song.objects.create(
        title = request.data["title"],
        album = request.data["album"],
        length = request.data["length"],
        artist_id=artist_id,
      )
      serializer = SongSerializer(song)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def update(self, request, pk):
        """Handle PUT requests for a song
        Returns:
            Response -- Empty body with 204 status code
        """
        song = Song.objects.get(pk=pk)
        song.title = request.data["title"]
        song.album = request.data["album"]
        song.length = request.data["length"]
        
        artist_id = Artist.objects.get(pk=request.data["artist_id"])
        song.artist_id = artist_id
        song.save()
        
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
      
    def destroy(self, request, pk):
        song = Song.objects.get(pk=pk)
        song.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class SongSerializer(serializers.ModelSerializer):
  """JSON serializer for songs"""
#   genres = SongGenreSerializer(many=True, read_only=True) - removed genres for single song view
  class Meta:
      model = Song
      fields = ('id', 'title', 'artist_id', 'album', 'length') # removed 'genres' from fields since only want it to be in the single song view
      depth = 0

# This detailed view of a single song and its info did not involve the use of joining tables, but sequentially piling on the required data in the correct order pulling it directly instead of joining serialized data:
class AllInfoSongSerializer(serializers.ModelSerializer):
    """JSON serializer for all info for a single song view"""
    artist = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = ('id', 'title', 'artist', 'album', 'length', 'genres')
        depth = 2
    
      
    def get_artist(self, song):
        artist_data = {
            'id': song.artist_id.id,
            'name': song.artist_id.name,
            'age': song.artist_id.age,
            'bio': song.artist_id.bio
        }
        return artist_data

    
    def get_genres(self, song):
        genres_data = [
            {'id': song_genre.genre_id.id, 
             'description': song_genre.genre_id.description} 
            for song_genre in song.songgenre_set.all()]
        return genres_data
