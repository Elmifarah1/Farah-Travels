# luxurytravels/models.py

from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    name = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(User, related_name='trips', on_delete=models.CASCADE)
    collaborators = models.ManyToManyField(User, related_name='collaborating_trips')

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')])
    trip = models.ForeignKey(Trip, related_name='tasks', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='tasks', on_delete=models.SET_NULL, null=True, blank=True)

class Notification(models.Model):
    user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
