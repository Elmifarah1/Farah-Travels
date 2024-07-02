from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Trip, Task, Notification
from .forms import TripForm, TaskForm

@login_required
def home(request):
    notifications = request.user.notifications.filter(read=False)
    return render(request, 'luxurytravels/home.html', {'notifications': notifications})

@login_required
def trip_list(request):
    trips = request.user.trips.all()
    return render(request, 'luxurytravels/trip_list.html', {'trips': trips})

@login_required
def trip_detail(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    return render(request, 'luxurytravels/trip_detail.html', {'trip': trip})

@login_required
def create_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.owner = request.user
            trip.save()
            form.save_m2m()
            return redirect('trip_list')
    else:
        form = TripForm()
    return render(request, 'luxurytravels/trip_form.html', {'form': form})

@login_required
def create_task(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.trip = trip
            task.save()
            return redirect('trip_detail', pk=trip.pk)
    else:
        form = TaskForm()
    return render(request, 'luxurytravels/task_form.html', {'form': form, 'trip': trip})

@login_required
def search_trips(request):
    query = request.GET.get('q')
    trips = Trip.objects.filter(name__icontains=query, owner=request.user)
    return render(request, 'luxurytravels/trip_list.html', {'trips': trips, 'query': query})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'luxurytravels/signup.html', {'form': form})

def landing(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'luxurytravels/landing.html')
