from blog.models import ArticleModel
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.forms import UpdateArticleForm

@login_required(login_url='/')
def updateArticle(request, slug):
    print(slug)
    article = get_object_or_404(ArticleModel, slug=slug, author=request.user)
    form = UpdateArticleForm(request.POST or None, files=request.FILES or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('detail', slug=article.slug)

    return render(request, 'pages/updateArticle.html',context={'form':form})