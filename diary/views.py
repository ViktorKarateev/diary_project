from rest_framework import viewsets
from .models import Entry, Tag, Mood
from .serializers import EntrySerializer, TagSerializer, MoodSerializer


class EntryViewSet(viewsets.ModelViewSet):
    """ViewSet для CRUD операций с записями дневника."""
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class TagViewSet(viewsets.ModelViewSet):
    """CRUD для тегов."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class MoodViewSet(viewsets.ModelViewSet):
    """CRUD для настроений."""
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer
