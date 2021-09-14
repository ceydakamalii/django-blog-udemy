from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from blog.forms import AddArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from blog.models import ArticleModel
from django.urls import reverse

class AddArticle(LoginRequiredMixin, CreateView):
    login_url=reverse_lazy('login')
    template_name = 'pages/addArticle.html'
    model = ArticleModel
    fields = ('title','content','image','categories')

    def get_success_url(self):
        return reverse('detail', kwargs={
            'slug':self.get_object().slug
        })
        

    def form_valid(self,form):
        article = form.save(commit=False)
        article.author = self.request.user
        article.save()
        form.save_m2m() #many to many relationships
        return super().form_valid(form)

"""
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
"""