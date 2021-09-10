from django import forms
from blog import models
from blog.models import ArticleModel

class AddArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        exclude = ('slug', 'author')
        