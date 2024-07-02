# luxurytravels/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),  # Landing page
    path('home/', views.home, name='home'),
    path('trips/', views.trip_list, name='trip_list'),
    path('trips/<int:pk>/', views.trip_detail, name='trip_detail'),
    path('trips/new/', views.create_trip, name='create_trip'),
    path('trips/<int:trip_id>/tasks/new/', views.create_task, name='create_task'),
    path('search/', views.search_trips, name='search_trips'),
    path('signup/', views.signup, name='signup'),
]
