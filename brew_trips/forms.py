from django.forms import ModelForm
from .models import BrewTrips

class BrewForm(ModelForm):
    class Meta():
        model = BrewTrips
        fields = ['brewery_city','brewery_name','brewery_address','brewery_url','favorite_brewery','latitude','longitude',]
