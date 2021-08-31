from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField
from autoslug import AutoSlugField
from blog.models import CategoryModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class ArticleModel(models.Model):
    image = models.ImageField(upload_to="article_images")
    title = models.CharField(max_length=100)
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from="title", unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name="article")
    author = models.ForeignKey(User, on_delete=CASCADE, related_name="articles")

    class Meta:
        verbose_name= "Article",
        verbose_name_plural="Articles"
        db_table="Article"

    def __str__(self):
        return self.title
