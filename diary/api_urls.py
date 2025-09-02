from django.urls import path, include
from rest_framework.routers import DefaultRouter
from diary.views import EntryViewSet, TagViewSet, MoodViewSet, TagSubscriptionViewSet, UserProfileView
from .views import RegisterAPIView


router = DefaultRouter()
router.register(r'entries', EntryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'moods', MoodViewSet)
router.register(r'tag-subscriptions', TagSubscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('register/', RegisterAPIView.as_view(), name='register'),
]
