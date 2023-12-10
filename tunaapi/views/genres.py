"""View module for handling requests about songs"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Genre


class GenreView(ViewSet):
      """Tuna api genre view"""
      def retrieve(self, request, pk):
        """Handle GET requests for single genre
        Returns:
          Response -- JSON serialized genre
          """
        try: 
            genre = Genre.objects.get(pk=pk)
            serializer = GenreWithSongsSerializer(genre)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Genre.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

      def list(self, request):
        """Handle GET requests to get all genres
        Returns:
            Response -- JSON serialized list of genres
        """
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True, context={'request': request})
        return Response(serializer.data)
      
      
      def create(self, request):
        """Handle POST operations for genres
        Returns:
            Response -- JSON serialized genre instance 
        """
        genre = Genre.objects.create(
            description=request.data["description"], 
        )
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
      
      def update(self, request, pk):
        """Handle PUT requests for a genre
        Returns:
            Response -- Empty body with 204 status code
        """
        genre = Genre.objects.get(pk=pk)
        genre.description = request.data["description"]
        genre.save()
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
      def destroy(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        genre.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class GenreSerializer(serializers.ModelSerializer):
    """JSON Serializer for genres"""

    class Meta:
        model = Genre
        fields = ('id', 'description')

class GenreWithSongsSerializer(serializers.ModelSerializer):
    """JSON serializer for genres with associated songs"""
    songs = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ('id', 'description', 'songs')

    
    def get_songs(self, genre):
        songs_data = [
            {
                'id': song.song_id.id,
                'title': song.song_id.title,
                'artist_id': song.song_id.artist_id.id,
                'album': song.song_id.album,
                'length': song.song_id.length,
            }
            for song in genre.songgenre_set.all()
        ]
        return songs_data
