from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trips/', views.trip_list, name='trip_list'),
    path('trips/<int:pk>/', views.trip_detail, name='trip_detail'),
    path('trips/new/', views.create_trip, name='create_trip'),
    path('trips/<int:pk>/edit/', views.update_trip, name='update_trip'),
    path('trips/<int:pk>/delete/', views.delete_trip, name='delete_trip'),
    path('search/', views.search_trips, name='search_trips'),
    path('profiles/', views.profile_list, name='profile_list'),  
    path('profiles/new/', views.create_profile, name='create_profile'),
    path('profiles/<int:pk>/', views.profile_detail, name='profile_detail'),
    path('profiles/<int:pk>/edit/', views.update_profile, name='update_profile'),
    path('profiles/<int:pk>/delete/', views.delete_profile, name='delete_profile'),  # Delete profile
]
