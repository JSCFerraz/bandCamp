from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from albums.models import Album
from rest_framework import generics


class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer

    def get_queryset(self):
        return Song.objects.filter(album=self.kwargs.get("pk"))

    def perform_create(self, serializer) -> None:
        album = get_object_or_404(Album, pk=self.kwargs.get("pk"))

        serializer.save(album_id=album.id)
