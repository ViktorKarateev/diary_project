from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from diary.models import Mood, Entry


User = get_user_model()


class EntryAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="user@example.com",
            password="testpass123",
            username="testuser"
        )
        self.client.login(email="user@example.com", password="testpass123")
        self.mood = Mood.objects.create(name="Радость", emoji="😊")

    def test_create_entry(self):
        self.client.force_authenticate(user=self.user)

        data = {
            "title": "Новая запись",
            "text": "Это текст записи",
            "mood": self.mood.id
        }
        response = self.client.post("/api/entries/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Entry.objects.count(), 1)
        self.assertEqual(Entry.objects.first().title, "Новая запись")

    def test_empty_text_validation(self):
        self.client.force_authenticate(user=self.user)

        data = {
            "title": "Неверная запись",
            "text": "   ",  # пустой текст
            "mood": self.mood.id
        }
        response = self.client.post("/api/entries/", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("text", response.data)
