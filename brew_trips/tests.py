from django.test import TestCase, Client

class BrewTest(TestCase):
    def setUp(self):
        self.client = Client()
        print('running a test')

    def test_getPath(self):
        self.client.get('/brewapi/', {'brewery_name': 'Central Coast Brewery', 'bar': 2})
        self.client.post('/brewapi/', {'name': 'stacey'}, follow=True)


class MyTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_route_when_logged_out(self):
        response = self.client.get('/brewapi/')
        self.assertEqual(response.status_code, 302)

    def test_route_when_logged_in(self):
        self.client.force_login(self.user)
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200) # 200. they should see the page
