from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import BrewTrips


class BrewTest(TestCase):
    def setUp(self):
        self.user = User(username="macey")
        self.user.save()
        self.client = Client()

    def test_getPath(self):
        self.client.get('/login/', {'username': 'macey', 'bar': 2})
        self.client.post('/signup/', {'name': 'stacey'}, follow=True)
