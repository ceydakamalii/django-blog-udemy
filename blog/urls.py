from django.urls import path, include
from blog.views import contact, home,myPosts,category

urlpatterns = [
    path('',home, name='home'),
    path('contact',contact, name='contact'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('myposts', myPosts, name='myposts')
]
