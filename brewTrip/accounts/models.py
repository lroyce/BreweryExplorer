from django.db import models
from django.utils import timezone

class BrewTrips(models.Model):
    brewery_name = models.CharField(max_length = 100)
    brewery_address = models.CharField(max_length = 100)
    brewery_url = models.CharField(max_length = 40)
    latitude = models.CharField(max_length = 20)
    longitude = models.CharField(max_length = 20)
    added_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    def prettify_datetime(self):
        return self.added_date.strftime('%b %b %y')
