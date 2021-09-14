from django.urls import path, include
from blog.views import ContactView, home,myPosts,CategoryListView,Detail,AddArticle,UpdateArticle,DeleteArticle, deleteComment
from django.views.generic import TemplateView, RedirectView
urlpatterns = [
    path('',home, name='home'),
    path('contact',ContactView.as_view(), name='contact'),
    path('category/<slug:categorySlug>', CategoryListView.as_view(), name='category'),
    path('myposts', myPosts, name='myposts'),
    path('detail/<slug:slug>', Detail.as_view(), name='detail'),
    path('add-article',AddArticle.as_view() , name='add-article'),
    path('update-article/<slug:slug>', UpdateArticle.as_view(), name='update-article'),
    path('delete-article/<slug:slug>', DeleteArticle.as_view(), name='delete-article'),
    path('delete-comment/<int:id>', deleteComment, name='delete-comment'),
    path('about',TemplateView.as_view(template_name='pages/about.html'), name='about'),
    path('redirect',RedirectView.as_view(url='https://www.google.com'), name='redirect'),
]
