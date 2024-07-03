from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Trip, Task
from .forms import TripForm, TaskForm

@login_required
def home(request):
    trips = request.user.trips.all()
    return render(request, 'luxurytravels/home.html', {'trips': trips})

@login_required
def task_management(request):
    tasks = Task.objects.filter(trip__owner=request.user)
    return render(request, 'luxurytravels/task_management.html', {'tasks': tasks})

@login_required
def trip_list(request):
    trips = request.user.trips.all()
    return render(request, 'luxurytravels/trip_list.html', {'trips': trips})

@login_required
def trip_detail(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    tasks = trip.tasks.all()
    return render(request, 'luxurytravels/trip_detail.html', {'trip': trip, 'tasks': tasks})

@login_required
def create_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.owner = request.user
            trip.save()
            return redirect('trip_list')
    else:
        form = TripForm()
    return render(request, 'luxurytravels/trip_form.html', {'form': form})

@login_required
def update_trip(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('trip_detail', pk=trip.pk)
    else:
        form = TripForm(instance=trip)
    return render(request, 'luxurytravels/trip_form.html', {'form': form})

@login_required
def delete_trip(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == 'POST':
        trip.delete()
        return redirect('trip_list')
    return render(request, 'luxurytravels/trip_confirm_delete.html', {'trip': trip})

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
def update_task(request, trip_id, task_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('trip_detail', pk=trip.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'luxurytravels/task_form.html', {'form': form, 'trip': trip})

@login_required
def delete_task(request, trip_id, task_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('trip_detail', pk=trip.pk)
    return render(request, 'luxurytravels/task_confirm_delete.html', {'task': task, 'trip': trip})

@login_required
def search_trips(request):
    query = request.GET.get('q')
    trips = Trip.objects.filter(name__icontains=query, owner=request.user)
    return render(request, 'luxurytravels/trip_list.html', {'trips': trips, 'query': query})
