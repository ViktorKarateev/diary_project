from rest_framework import serializers
from .models import Entry, Tag, Mood


class EntrySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Entry."""

    class Meta:
        model = Entry
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    """Сериализатор для тега."""

    class Meta:
        model = Tag
        fields = '__all__'


class MoodSerializer(serializers.ModelSerializer):
    """Сериализатор для настроения."""

    class Meta:
        model = Mood
        fields = '__all__'