from rest_framework import viewsets
from .models import Entry
from .serializers import EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    """ViewSet для CRUD операций с записями дневника."""
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
