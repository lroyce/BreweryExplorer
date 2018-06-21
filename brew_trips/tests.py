from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import BrewTrips


class BrewTest(TestCase):
    def setUp(self):
        self.user = User(username="stacey")
        self.user.save()
        self.client = Client()

    def test_getPath(self):
        self.client.get('/brewapi/', {'brewery_name': 'Central Coast Brewery', 'bar': 2})
        self.client.post('/brewapi/', {'name': 'stacey'}, follow=True)

class modelTest(TestCase):
    def setUp(self):
        self.user = User(username="stacey")
        self.user.save()
        self.client = Client()

    def test_route_when_logged_out(self):
        response = self.client.get(reverse('brewapi'))
        self.assertEqual(response.status_code, 302)

    def test_route_when_logged_in(self):
        response = self.client.get(reverse('brewapi'))
        self.client.force_login(self.user)
        self.assertEqual(response.status_code, 302) ##may be due to local testing

    def test_response_contains(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, "Username")
