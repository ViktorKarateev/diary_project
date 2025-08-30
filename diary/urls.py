from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EntryViewSet, TagViewSet, MoodViewSet, UserProfileView, TagSubscriptionViewSet

router = DefaultRouter()
router.register(r'entries', EntryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'moods', MoodViewSet)
router.register(r'tag-subscriptions', TagSubscriptionViewSet, basename='tag-subscriptions')


urlpatterns = [
    path('', include(router.urls)),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
