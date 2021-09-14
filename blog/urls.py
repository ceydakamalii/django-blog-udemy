from django.urls import path, include
from blog.views import contact, home,myPosts,CategoryListView,Detail,addArticle,updateArticle,DeleteArticle, deleteComment
from django.views.generic import TemplateView, RedirectView
urlpatterns = [
    path('',home, name='home'),
    path('contact',contact, name='contact'),
    path('category/<slug:categorySlug>', CategoryListView.as_view(), name='category'),
    path('myposts', myPosts, name='myposts'),
    path('detail/<slug:slug>', Detail.as_view(), name='detail'),
    path('add-article',addArticle , name='add-article'),
    path('update-article/<slug:slug>', updateArticle, name='update-article'),
    path('delete-article/<slug:slug>', DeleteArticle.as_view(), name='delete-article'),
    path('delete-comment/<int:id>', deleteComment, name='delete-comment'),
    path('about',TemplateView.as_view(template_name='pages/about.html'), name='about'),
    path('redirect',RedirectView.as_view(url='https://www.google.com'), name='redirect'),
]
