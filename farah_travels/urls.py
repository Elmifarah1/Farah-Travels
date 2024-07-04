# farah_travels/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('luxurytravels.urls')),  
    path('accounts/', include('allauth.urls')),  
    path('', include('luxurytravels.urls')),     
]
