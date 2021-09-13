from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def logout(request):
    django_logout(request)
    return redirect('home')