# farah_travels/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Include allauth URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django auth URLs
    path('', include('luxurytravels.urls')),     # Include your app URLs
]
