from django.test import TestCase
from diary.models import Mood
from diary.serializers import MoodSerializer

class MoodSerializerTest(TestCase):
    def test_serializer_fields(self):
        mood = Mood.objects.create(name="Счастье", emoji="😄")
        serializer = MoodSerializer(mood)

        expected_data = {
            "id": mood.id,
            "name": "Счастье",
            "emoji": "😄",
        }

        self.assertEqual(serializer.data, expected_data)
