from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BrewForm
from .models import BrewTrips
from django.conf import settings
import requests


def home(request):
    context = {
    'title':'Welcome To Your Trips',
    'breweries': BrewTrips.objects.order_by('-added_date'),
    }
    return render(request, 'home.html', context)

@login_required
def brewmap(request):
    key = settings.BEER_MAP_KEY
    locations = {}
    if key:
        call = requests.get(f"http://beermapping.com/webservice/loccity/{key}/portland,or&s=json")
        locations = call.json()
        if request.method == 'POST':
            plan_form = BrewForm(data=request.POST)
            if plan_form.is_valid():
                plan = plan_form.save(commit=False)
                plan.brew_user = request.user
                plan.save()
                return redirect('home')
        else:
            plan_form = BrewForm()

        return render(request, 'brewmap.html', {
        'locations':locations,
        })
#
# def create(request):
#     if request.method == 'POST':
#         plan_form = BrewForm(data=request.POST)
#         if plan_form.is_valid():
#             plan = plan_form.save(commit=False)
#             plan.brew_user = request.user
#             plan.save()
#             return redirect('home')
#     else:
#         plan_form = BrewForm()
#
#     return render(request, 'create.html', {
#     'title':'Add a new trip',
#     'plan_form': plan_form
#     })

@login_required
def delete(request,id):
    if request.method == 'POST':
        plan = get_object_or_404(BrewTrips,pk=id)
        plan.delete()
        return redirect('home')


# def brewMap(request):
#     key = settings.BEER_MAP_KEY
#     locations = {}
#     if key:
#         call = requests.get(f"http://beermapping.com/webservice/loccity/{key}/eugene,or&s=json")
#         locations = call.json()
#         print(locations[0])
#     return render(request, 'create.html', {'locations':locations})
