from django.shortcuts import redirect, render
from blog.forms import AddArticleForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def addArticle(request):
    form = AddArticleForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        form.save_m2m() #many to many relationships
        return redirect('detail', slug=article.slug) 
    return render(request, 'pages/addArticle.html',context={'form':form})