from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def myPosts(request):
    
    articles = request.user.articles.order_by('id')
    print(articles)
    page = request.GET.get('page')
    paginator = Paginator(articles, 2)
    context={
        'articles': paginator.get_page(page)
    }
    return render(request, 'pages/myposts.html', context=context)