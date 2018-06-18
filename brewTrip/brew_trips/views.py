from django.shortcuts import render, redirect, get_object_or_404
from .forms import BrewForm
from .models import BrewTrips
from django.contrib.auth.decorators import login_required


def home(request):
    context = {
    'title':'Welcome To Your Trips',
    'breweries': BrewTrips.objects.order_by('added_date'),
    }
    return render(request, 'home.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        plan_form = BrewForm(data=request.POST)
        if plan_form.is_valid():
            plan = plan_form.save(commit=False)
            # We'll set commit=False so we can populate our model with non model form data
            plan.brew_user = request.user
            # Now we can insert the logged in user, they were attached to the request body
            plan.save()
            return redirect('home')
    else:
        plan_form = BrewForm()

    return render(request, 'createPlan.html', {
    'title':'Add a new trip',
    'plan_form': plan_form
    })



@login_required
def delete(request, plan_id):
    if request.method == 'POST':
        plan = get_object_or_404(BrewTrips, pk=plan_id)
        plan.delete()
        return redirect('home', user_id=request.user.id)
