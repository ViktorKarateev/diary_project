from django.test import TestCase
from django.contrib.auth import get_user_model
from diary.models import Entry, Mood
from diary.serializers import EntrySerializer
from rest_framework.test import APIRequestFactory

User = get_user_model()


class EntryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            password='1234',
            username='testuser',  # добавили username
        )
        self.mood = Mood.objects.create(name='Радость', emoji='😊')

    def test_str_representation(self):
        entry = Entry.objects.create(
            user=self.user,
            title='Моя запись',
            text='Содержимое',
            mood=self.mood,
        )
        self.assertIn('Моя запись', str(entry))


class EntrySerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test2@example.com',
            password='1234',
            username='testuser2',
        )
        self.factory = APIRequestFactory()
        self.request = self.factory.post('/entries/', {})
        self.request.user = self.user

    def test_empty_text_validation(self):
        data = {
            'title': 'Тестовая запись',
            'text': '   ',
        }
        serializer = EntrySerializer(
            data=data,
            context={'request': self.request},
        )
        self.assertFalse(serializer.is_valid())
        self.assertIn('text', serializer.errors)
