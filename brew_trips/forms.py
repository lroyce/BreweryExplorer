from django.forms import ModelForm
from .models import BrewTrips

class BrewForm(ModelForm):
    class Meta():
        model = BrewTrips
        fields = ['brewery_name','brewery_address','brewery_url','latitude','longitude',]
