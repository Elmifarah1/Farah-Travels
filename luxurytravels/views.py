# luxurytravels/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Trip, Profile
from .forms import TripForm, ProfileForm
from django.db.models import Q
from django.contrib import messages

@login_required
def home(request):
    return render(request, 'luxurytravels/home.html')

@login_required
def trip_list(request):
    trips = Trip.objects.filter(owner=request.user)
    return render(request, 'luxurytravels/trip_list.html', {'trips': trips})

@login_required
def trip_detail(request, pk):
    trip = get_object_or_404(Trip, pk=pk, owner=request.user)
    return render(request, 'luxurytravels/trip_detail.html', {'trip': trip})

@login_required
def create_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.owner = request.user
            trip.save()
            messages.success(request, 'Trip created successfully!')
            return redirect('trip_list')
    else:
        form = TripForm()
    return render(request, 'luxurytravels/create_trip.html', {'form': form})

@login_required
def update_trip(request, pk):
    trip = get_object_or_404(Trip, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trip updated successfully!')
            return redirect('trip_detail', pk=trip.pk)
    else:
        form = TripForm(instance=trip)
    return render(request, 'luxurytravels/update_trip.html', {'form': form})

@login_required
def delete_trip(request, pk):
    trip = get_object_or_404(Trip, pk=pk, owner=request.user)
    if request.method == 'POST':
        trip.delete()
        messages.success(request, 'Trip deleted successfully!')
        return redirect('trip_list')
    return render(request, 'luxurytravels/delete_trip.html', {'trip': trip})

@login_required
def search_trips(request):
    query = request.GET.get('q')
    if query:
        trips = Trip.objects.filter(Q(destination__icontains=query) | Q(name__icontains=query))
    else:
        trips = Trip.objects.none()
    return render(request, 'luxurytravels/trip_list.html', {'trips': trips})


@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'luxurytravels/profile.html', {'form': form})