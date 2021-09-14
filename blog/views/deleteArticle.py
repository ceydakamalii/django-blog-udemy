from blog.models import ArticleModel
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.urls import reverse_lazy

class DeleteArticle(DeleteView):
    
    template_name = 'pages/delete_article_confirmation.html'
    success_url = reverse_lazy('myposts')
    def get_queryset(self):
        article = ArticleModel.objects.filter(slug=self.kwargs['slug'], author=self.request.user)
        return article
        


"""
@login_required(login_url='/')
def deleteArticle(request, slug):
    get_object_or_404(ArticleModel, slug=slug, author=request.user).delete()
    return redirect('myposts')

"""