from django.shortcuts import render
from blog.models import ArticleModel
from django.core.paginator import Paginator
def home(request):
    articles = ArticleModel.objects.order_by("-id")
    page = request.GET.get('page')
    paginator = Paginator(articles, 2)
    context={
        'articles': paginator.get_page(page)
    }
    return render(request, 'pages/home.html', context=context)