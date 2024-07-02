# luxurytravels/forms.py

from django import forms
from .models import Trip, Task

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['name', 'destination', 'start_date', 'end_date', 'collaborators']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date', 'priority', 'assigned_to']