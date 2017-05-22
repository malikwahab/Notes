from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from notes.serializers import NoteSerializer
from notes.models import Note
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from notes.permissions import IsOwnerOrReadOnly
# Create your views here.


class NoteViewSet(ModelViewSet):

    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
