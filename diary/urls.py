from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EntryViewSet, TagViewSet, MoodViewSet

router = DefaultRouter()
router.register(r'entries', EntryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'moods', MoodViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
