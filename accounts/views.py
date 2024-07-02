from django.contrib.auth.views import LogoutView
from django.views.generic import View
from django.http import HttpResponseRedirect

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        # Perform the logout and redirect to the logout redirect URL
        return self.post(request, *args, **kwargs)