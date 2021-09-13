from django.urls import path
from account.views import logout, changePassword,editProfile

urlpatterns = [
    path('logout', logout, name='logout'),
    path('change-password', changePassword, name='change-password'),
    path('edit-profile', editProfile, name='edit-profile'),
]