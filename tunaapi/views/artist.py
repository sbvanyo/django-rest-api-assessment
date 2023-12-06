from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Artist

class ArtistView(ViewSet):

    def retrieve(self, request, pk):
        return Response({})

    def list(self, request):
        return Response({})

    def create(self, request):
        return Response({})

    def delete(self, request, pk):
        return Response({})

    def update(self, request, pk):
        return Response({})


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name')