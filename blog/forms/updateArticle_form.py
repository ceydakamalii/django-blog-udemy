from django import forms
from blog.models import ArticleModel

class UpdateArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        exclude = ('slug', 'author')
        