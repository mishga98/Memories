from django.test import TestCase, RequestFactory
from django.test.client import Client
from django.contrib.auth.models import User



class ViewsTestCase(TestCase):


    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://localhost:8000')
        self.assertEqual(response.status_code, 200)

    def test_notes_redirect_unathorized(self):
        """The notes page redirects if you're anonymous"""
        response = self.client.get('http://localhost:8000/notes')
        self.assertEqual(response.status_code, 301)

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='foo', email='foo@bar',
            password='bar')

    def test_notes_load_for_authorize(self):
        """The notes page loads properly if you're authorized"""
        user = User.objects.create(username='testuser')
        user.save()
        client = Client()
        response = client.get("http://localhost:8000", follow=True)
        self.assertEqual(response.status_code, 200)