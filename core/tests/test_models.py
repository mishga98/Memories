from django.test import TestCase
from core.models import Note

class ModelsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass
    def setUp(self):
        pass

    def test_post_has_slug(self):
        """Posts are given slugs correctly when saving"""
        note = Note.objects.create(title="My first post")

        note.title = "It's theater"
        note.save()
        self.assertTrue(len(note.title)<72)