# luxurytravels/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home view
    path('trips/', views.trip_list, name='trip_list'),  # List trips
    path('trips/<int:pk>/', views.trip_detail, name='trip_detail'),  # Trip detail
    path('trips/new/', views.create_trip, name='create_trip'),  # Create trip
    path('trips/<int:pk>/edit/', views.update_trip, name='update_trip'),  # Update trip
    path('trips/<int:pk>/delete/', views.delete_trip, name='delete_trip'),  # Delete trip
    path('trips/<int:trip_id>/tasks/new/', views.create_task, name='create_task'),  # Create task for a trip
    path('trips/<int:trip_id>/tasks/<int:task_id>/edit/', views.update_task, name='update_task'),  # Update task
    path('trips/<int:trip_id>/tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),  # Delete task
    path('search/', views.search_trips, name='search_trips'),  # Search trips
    path('task_management/', views.task_management, name='task_management'),  # Task management view

]
