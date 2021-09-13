from django import forms
from blog.models import CommentModel

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('comment', )