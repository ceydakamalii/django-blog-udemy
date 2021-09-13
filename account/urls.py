from django.urls import path
from account.views import logout

urlpatterns = [
    path('logout', logout, name='logout')
]