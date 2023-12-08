"""View module for handling requests about artists"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Artist


class ArtistView(ViewSet):
    """Tuna artists view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single artist

        Returns:
            Response -- JSON serialized artist
        """
        artist = Artist.objects.get(pk=pk)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all artists

        Returns:
            Response -- JSON serialized list of artists
        """
        artists = Artist.objects.all()
        
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)
      
    
    ########################
    ######## CREATE ########
    ########################
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized artist instance
        """

        artist = Artist.objects.create(
            name=request.data["name"],
            age=request.data["age"],
            bio=request.data["bio"],
        )
        serializer = ArtistSerializer(artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    ########################
    ######## UPDATE ########
    ########################
   
    def update(self, request, pk):
        """Handle PUT requests for an artist

        Returns:
            Response -- Empty body with 204 status code
        """

        artist = Artist.objects.get(pk=pk)
        artist.name = request.data["name"]
        artist.age = request.data["age"]
        artist.bio = request.data["bio"]

        artist.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    ########################
    ######## DELETE ########
    ########################

    def destroy(self, request, pk):
        """Handle delete requests for an artist"""

        artist = Artist.objects.get(pk=pk)
        artist.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ArtistSerializer(serializers.ModelSerializer):
    """JSON serializer for artists
    """
    class Meta:
        model = Artist
        fields = ('id', 'name', 'age', 'bio')
