from blog.models import ArticleModel
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
@login_required(login_url='/')
def deleteArticle(request, slug):
    get_object_or_404(ArticleModel, slug=slug, author=request.user).delete()
    return redirect('myposts')

