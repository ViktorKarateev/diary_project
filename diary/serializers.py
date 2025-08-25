from rest_framework import serializers
from .models import Entry


class EntrySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Entry."""

    class Meta:
        model = Entry
        fields = '__all__'
