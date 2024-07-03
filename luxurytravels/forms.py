# luxurytravels/forms.py

from django import forms
from .models import Trip, Task

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['name', 'destination', 'travel_date', 'return_date', 'num_people', 'departure_airport', 'description']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'completed']