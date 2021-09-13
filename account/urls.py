from django.urls import path
from account.views import logout, changePassword

urlpatterns = [
    path('logout', logout, name='logout'),
     path('change-password', changePassword, name='change-password'),
]