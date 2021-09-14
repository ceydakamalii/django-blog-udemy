from django.urls.base import reverse_lazy
from blog.models import ArticleModel
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import UpdateArticleForm
from django.views.generic import UpdateView
from django.urls import reverse, reverse_lazy

class UpdateArticle(LoginRequiredMixin, UpdateView):
    login_url=reverse_lazy('login')
    template_name = 'pages/updateArticle.html'
    fields = ('title','content','image','categories')

    def get_object(self):
        article=get_object_or_404(ArticleModel, slug=self.kwargs.get('slug'), author=self.request.user)
        return article

    def get_success_url(self):
        return reverse('detail',kwargs={
            'slug':self.get_object().slug
        })

   


"""
@login_required(login_url='/')
def updateArticle(request, slug):
    print(slug)
    article = get_object_or_404(ArticleModel, slug=slug, author=request.user)
    form = UpdateArticleForm(request.POST or None, files=request.FILES or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('detail', slug=article.slug)

    return render(request, 'pages/updateArticle.html',context={'form':form})
"""