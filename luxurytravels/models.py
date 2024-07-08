# luxurytravels/models.py
from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    travel_date = models.DateField()
    return_date = models.DateField()
    num_people = models.PositiveIntegerField()
    departure_airport = models.CharField(max_length=100)
    owner = models.ForeignKey(User, related_name='trips', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} to {self.destination}"

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    trip = models.ForeignKey(Trip, related_name='tasks', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Notification(models.Model):
    user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
    dob = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    passport_number = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username