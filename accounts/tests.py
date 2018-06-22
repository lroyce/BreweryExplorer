from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.contrib.auth.models import User
from io import BytesIO
# from ..models import BrewTrips


class AccountsTest(TestCase):
    def setUp(self):
        self.user = User(username="macey")
        self.user.save()
        self.client = Client()

    def test_getPath(self):
        self.client.get('/login/', {'username': 'macey', 'bar': 2})
        self.client.post('/signup/', {'name': 'stacey'}, follow=True)

    def test_get(self):
        self.client.get('', {'foo': 1, 'bar': 2})

    def test_index(self):
        client = Client()
        response = client.get('/signup/')
        self.assertEqual(response.status_code, 404)
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 404)
#this fails but may be due to local deloyment
    @override_settings(LOGIN_URL='/login/')
    def test_login(self):
        response = self.client.get('/sekrit/')
        self.assertRedirects(response, '/login/?next=/sekrit/')
