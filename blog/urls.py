from blog.views.detail import detail
from django.urls import path, include
from blog.views import contact, home,myPosts,category,detail,addArticle,updateArticle,deleteArticle

urlpatterns = [
    path('',home, name='home'),
    path('contact',contact, name='contact'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('myposts', myPosts, name='myposts'),
    path('detail/<slug:slug>', detail, name='detail'),
    path('add-article',addArticle , name='add-article'),
    path('update-article/<slug:slug>', updateArticle, name='update-article'),
    path('delete-article/<slug:slug>', deleteArticle, name='delete-article'),
]
