from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BrewTrips(models.Model):
    brewery_city = models.CharField(max_length = 40,blank=True)
    brewery_name = models.CharField(max_length = 100)
    brewery_address = models.CharField(max_length = 100)
    brewery_url = models.CharField(max_length = 40)
    favorite_brewery = models.BooleanField(default=False)
    latitude = models.CharField(max_length = 20,blank=True)
    longitude = models.CharField(max_length = 20,blank=True)
    added_date = models.DateTimeField(default=timezone.now)
    brew_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.brewery_name
    def prettify_datetime(self):
        return self.added_date.strftime('%B %e %Y')
