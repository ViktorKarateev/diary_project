# diary/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (EntryViewSet, TagViewSet, MoodViewSet,UserProfileView, TagSubscriptionViewSet,EntryCreateView, EntryListView)

app_name = 'diary'

router = DefaultRouter()
router.register(r'entries', EntryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'moods', MoodViewSet)
router.register(r'tag-subscriptions', TagSubscriptionViewSet, basename='tag-subscriptions')

urlpatterns = [
    path('api/', include(router.urls)),  # <-- только API сюда
    path('api/profile/', UserProfileView.as_view(), name='profile'),
    path('entries/', EntryListView.as_view(), name='entry_list'),
    path('entries/new/', EntryCreateView.as_view(), name='entry_create'),  # <-- HTML-форма
]

