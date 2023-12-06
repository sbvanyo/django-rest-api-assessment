from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Genre

class GenreView(ViewSet):

    def retrieve(self, request, pk):
        pass

    def list(self, request):
        pass

    def create(self, request):
        pass

    def delete(self, request, pk):
        pass

    def update(self, request, pk):
        pass