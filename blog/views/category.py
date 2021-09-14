from django.shortcuts import render, get_object_or_404
from blog.models import ArticleModel, CategoryModel
from django.core.paginator import Paginator
from django.views.generic import ListView

class CategoryListView(ListView):
    template_name = 'pages/category.html'
    context_object_name = 'articles'
    paginate_by = 2

    def get_queryset(self):
        category = get_object_or_404(CategoryModel, slug=self.kwargs['categorySlug'])
        return category.article.all().order_by('-id')

        


"""
def category(request, categorySlug):
    category=get_object_or_404(CategoryModel, slug=categorySlug)
    articles = category.article.order_by('-id')
    print(articles)
    page = request.GET.get('page')
    paginator = Paginator(articles, 2)
    context={
        'articles': paginator.get_page(page),
        'category_name': category.name
    }
    return render(request, 'pages/category.html', context=context)
"""