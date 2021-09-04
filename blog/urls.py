from django.urls import path, include
from blog.views import contact, home

urlpatterns = [
    path('',home),
    path('contact',contact),
]
