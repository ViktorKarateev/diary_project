from rest_framework import serializers
from .models import Entry, Tag, Mood
from django.contrib.auth import get_user_model

User = get_user_model()

class EntrySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Entry."""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

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


class UserProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для профиля пользователя."""

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']
        read_only_fields = ['id', 'email']  # Email только для чтения