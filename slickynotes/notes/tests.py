from django.test import TestCase
from notes.models import Note
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
