from rest_framework import serializers
from .models import Entry, Tag, Mood, TagSubscription
from django.contrib.auth import get_user_model


User = get_user_model()


class EntrySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Entry
        fields = '__all__'

    def validate_text(self, value):
        """Запрещаем пустые или пробельные записи."""
        if not value.strip():
            raise serializers.ValidationError("Поле 'text' не может быть пустым.")
        return value


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


class TagSubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор для подписки на тег."""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TagSubscription
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user
