# diary/views.py
from rest_framework import viewsets, permissions
from .models import Entry, Tag, Mood, TagSubscription
from .serializers import EntrySerializer, TagSerializer, MoodSerializer, UserProfileSerializer, TagSubscriptionSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import RetrieveUpdateAPIView
from django.contrib.auth import get_user_model


User = get_user_model()


class EntryViewSet(viewsets.ModelViewSet):
    """ViewSet для CRUD операций с записями дневника."""
    queryset = Entry.objects.none()  # ← нужно для router, даже если не используется
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Возвращаем только записи текущего пользователя
        return Entry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Привязываем пользователя автоматически
        serializer.save(user=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    """CRUD для тегов."""
    queryset = Tag.objects.all()  # ← ОБЯЗАТЕЛЬНО
    serializer_class = TagSerializer


class MoodViewSet(viewsets.ModelViewSet):
    """CRUD для настроений."""
    queryset = Mood.objects.all()  # ← ОБЯЗАТЕЛЬНО
    serializer_class = MoodSerializer


class UserProfileView(RetrieveUpdateAPIView):
    """
    Профиль текущего пользователя.
    GET  /api/profile/    — получить свой профиль
    PATCH/PUT /api/profile/ — обновить first_name, last_name
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # всегда возвращаем текущего пользователя
        return self.request.user


class TagSubscriptionViewSet(viewsets.ModelViewSet):
    """API для управления подписками на теги."""

    serializer_class = TagSubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TagSubscription.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
