from django.test import TestCase
from core.forms import NoteForm

class RenewBookFormTest(TestCase):

    def test_UserForm_valid(self):
        form = NoteForm(data={'person': "user", 'title': 'title', 'note': 'description', 'coordinates':'55.3234, 52.23434'})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = NoteForm(data={'person': "user", 'title': '', 'note': 'description', 'coordinates': '55.3234, 52.23434'})
        self.assertFalse(form.is_valid())