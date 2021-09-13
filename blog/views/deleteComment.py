from blog.models import CommentModel
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='/')
def deleteComment(request, id):
    comment= get_object_or_404(CommentModel, id=id)
    if comment.author==request.user or comment.article.author==request.user:
        comment.delete()
        messages.success(request, 'Comment successfully deleted')
        return redirect('detail',slug=comment.article.slug)
    return redirect('myposts')

