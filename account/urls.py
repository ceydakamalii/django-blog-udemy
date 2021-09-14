from django.urls import path
from account.views import logout, changePassword,editProfile,signup,ProfileDetailView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('logout', logout, name='logout'),
    path('change-password', changePassword, name='change-password'),
    path('edit-profile', editProfile, name='edit-profile'),
    path('signup', signup, name='signup'),
    path('login',auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('user/<str:username>', ProfileDetailView.as_view(), name='profile'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)