from django.shortcuts import render, get_object_or_404,redirect
from blog.models import ArticleModel
from blog.forms import AddCommentForm
from django.views import View
from django.contrib import messages
import logging

logger = logging.getLogger('text_reading')

class Detail(View):

    http_method_names = ['get', 'post']
    add_comment_form = AddCommentForm
    
    def get(self, request, slug):
        #print(1/0) sentry 
        post = get_object_or_404(ArticleModel, slug=slug)
        if request.user.is_authenticated:
            logger.info('Article Read : '+request.user.username)
        comments = post.comments.all()
        return render(request,'pages/detail.html',context={
        'post':post,
        'comments':comments,
        'add_comment_form':self.add_comment_form(),
    })

    def post(self, request, slug):
        post = get_object_or_404(ArticleModel, slug=slug)
        add_comment_form =self.add_comment_form(request.POST)
        if add_comment_form.is_valid():
            comment= add_comment_form.save(commit=False)
            comment.author= request.user
            comment.article= post
            comment.save()
            messages.success(request,'Comment successfully added' )
        return redirect('detail',slug=slug)


"""
def detail(request, slug):

    post = get_object_or_404(ArticleModel, slug=slug)
    comments = post.comments.all()
    if request.method == 'POST' :
        add_comment_form = AddCommentForm(data=request.POST)
        if add_comment_form.is_valid():
            comment= add_comment_form.save(commit=False)
            comment.author= request.user
            comment.article= post
            comment.save()
   
    add_comment_form = AddCommentForm()

    return render(request, 'pages/detail.html',context={
        'post':post,
        'comments':comments,
        'add_comment_form':add_comment_form
    })
"""