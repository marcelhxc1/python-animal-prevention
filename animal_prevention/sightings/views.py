from django.shortcuts import render, redirect
from .forms import SightingForm
from .models import Sighting

def home(request):
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('sighting_list') 
    else:
        form = SightingForm()
    return render(request, 'sightings/home.html', {'form': form})

def sighting_list(request):
    sightings = Sighting.objects.all() 
    return render(request, 'sightings/sighting_list.html', {'sightings': sightings})
