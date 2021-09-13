from django.urls import path
from account.views import logout, changePassword,editProfile,signup
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('logout', logout, name='logout'),
    path('change-password', changePassword, name='change-password'),
    path('edit-profile', editProfile, name='edit-profile'),
    path('signup', signup, name='signup'),
    path('login',auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    
]