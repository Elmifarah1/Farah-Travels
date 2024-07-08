# luxurytravels/forms.py

from django import forms
from .models import Trip, Task, Profile

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['name', 'destination', 'travel_date', 'return_date', 'num_people', 'departure_airport', 'description']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'completed']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'address', 'dob', 'phone', 'passport_number', 'frequent_flyer_number', 'emergency_contact_name', 'emergency_contact_phone']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }
