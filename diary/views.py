# diary/views.py
from rest_framework import viewsets, permissions, filters, generics
from .models import Entry, Tag, Mood, TagSubscription
from .serializers import EntrySerializer, TagSerializer, MoodSerializer, UserProfileSerializer, TagSubscriptionSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import RetrieveUpdateAPIView
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.db.models import Q


User = get_user_model()


class EntryViewSet(viewsets.ModelViewSet):
    """ViewSet для CRUD операций с записями дневника."""
    queryset = Entry.objects.none()  # ← нужно для router, даже если не используется
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['mood', 'tags']
    ordering_fields = ['created_at']

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
    queryset = TagSubscription.objects.all()

    def get_queryset(self):
        return TagSubscription.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class EntryCreateView(CreateView):
    model = Entry
    fields = ['title', 'text', 'mood', 'tags']
    template_name = 'diary/entry_form.html'
    success_url = reverse_lazy('entry_create')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EntryListView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'diary/entries_list.html'
    context_object_name = 'entries'

    def get_queryset(self):
        queryset = Entry.objects.filter(user=self.request.user).select_related('mood').prefetch_related(
            'tags').order_by('-created_at')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(text__icontains=query)
            )
        return queryset

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = []


class EntryUpdateView(LoginRequiredMixin, UpdateView):
    model = Entry
    fields = ['title', 'text', 'mood', 'tags']
    template_name = 'diary/entry_form.html'
    success_url = reverse_lazy('entry_list')

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user)


class EntryDeleteView(LoginRequiredMixin, DeleteView):
    model = Entry
    template_name = 'diary/entry_confirm_delete.html'
    success_url = reverse_lazy('entry_list')

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user)
