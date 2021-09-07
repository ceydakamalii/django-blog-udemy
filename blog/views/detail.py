from django.shortcuts import render, get_object_or_404
from blog.models import ArticleModel

def detail(request, slug):
    post = get_object_or_404(ArticleModel, slug=slug)
    comments = post.comments.all()
    return render(request, 'pages/detail.html',context={
        'post':post,
        'comments':comments
    })