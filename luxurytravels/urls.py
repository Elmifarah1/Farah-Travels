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
    path('profile/', views.profile_view, name='profile_view'),
]
