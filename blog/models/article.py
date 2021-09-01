from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel
from ckeditor.fields import RichTextField

class ArticleModel(models.Model):
    image = models.ImageField(upload_to="article_images")
    title = models.CharField(max_length=100)
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from="title", unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name="article")
    author = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name="articles")

    class Meta:
        verbose_name= "Article",
        verbose_name_plural="Articles"
        db_table="Article"

    def __str__(self):
        return self.title
