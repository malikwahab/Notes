from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from notes.models import Note
from notes.serializers import NoteSerializer
from django.contrib.auth.models import User
# Create your tests here.


class TestModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='malikwahab',
                                             password='test')

    def test__str__(self):
        note = Note.objects.create(title="A simple Note",
                                   content="A Jot during assessment",
                                   owner=self.user)
        self.assertEqual(note.__str__(), "A simple Note")


class TestSerializers(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='malikwahab',
                                             password='test')
        self.note = Note.objects.create(title="A simple Note",
                                        content="A Jot during assessment",
                                        owner=self.user)

    def test_is_valid(self):
        note_serializer = NoteSerializer(instance=self.note)
        serializer_data = note_serializer.data
        test_serializer = NoteSerializer(data=serializer_data)
        self.assertTrue(test_serializer.is_valid())


class NoteViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='malikwahab',
                                             password='test')
        self.client = APIClient()
        self.client.login(username="malikwahab", password="test")
        self.note = Note.objects.create(title="A simple Note",
                                        content="A Jot during assessment",
                                        owner=self.user)

    def test_create_note(self):
        response = self.client.post('/api/v1/notes/', {'title': 'A Test',
                                    'content': 'A brief test'})
        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'A Test')

    def test_create_more_content(self):
        response = self.client.post('/api/v1/notes/', {'title': 'A Test',
                                    'content': 'Test'*100})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_notes(self):
        response = self.client.get('/api/v1/notes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
