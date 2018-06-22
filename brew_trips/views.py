import requests
from .forms import BrewForm
from .models import BrewTrips
from django.conf import settings
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User


@login_required
def home(request):
    user = request.user
    id = user.id
    # https://stackoverflow.com/questions/20256909/django-how-to-write-query-to-sort-using-multiple-columns-display-via-template/20257999#20257999
    user_breweries = BrewTrips.objects.filter(brew_user_id=id).order_by('brewery_city','added_date')

    context = {
    'title':f'Hello {user.first_name}',
    'breweries': user_breweries
    }
    return render(request, 'home.html', context)


@login_required
def favorites(request):
    user = request.user
    id = user.id
    # https://stackoverflow.com/questions/20256909/django-how-to-write-query-to-sort-using-multiple-columns-display-via-template/20257999#20257999
    user_breweries = BrewTrips.objects.filter(brew_user_id=id, favorite_brewery=True).order_by('brewery_city','added_date')
    context = {
    'title':f'Hello {user.first_name}',
    'breweries': user_breweries
    }
    return render(request, 'favorites.html', context)


@login_required
def brewapi(request):
    key = settings.BEER_MAP_KEY
    locations = {}
    if 'city-search' in request.GET:
        city = request.GET['city-search']
        city = whitespace(city)
        url = f"http://beermapping.com/webservice/loccity/{key}/{city}&s=json"
        print(url)
        call = requests.get(url)
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

    return render(request,'brewapi.html', {
    'locations':locations,
    })


###needed a quick method to help with white space after comma in city search##
def whitespace(str):
    if ", " in str:
        return str.replace(", ", ",")
    else:
        return str


# @login_required
# def brewmap(request):
#     user = request.user
#     id = user.id
#     user_breweries = BrewTrips.objects.filter(brew_user_id=id)
#     context = {
#     'title':'Welcome To Your Trips',
#     'breweries': user_breweries.order_by('brewery_city'),
#     # 'breweries': user_breweries,
#     }
#     return render(request, 'brewmap.html', context)


@login_required
def delete(request,id):
    if request.method == 'POST':
        plan = get_object_or_404(BrewTrips,pk=id)
        plan.delete()
        return redirect('home')


@login_required
def update(request, id):
    print(id)
    if request.method == 'POST':
        brew = get_object_or_404(BrewTrips, pk=id)
        if brew.favorite_brewery:
            brew.favorite_brewery = False
        else:
            brew.favorite_brewery = True
        brew.save()
    return redirect('home')
