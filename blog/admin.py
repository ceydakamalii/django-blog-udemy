from django.contrib import admin
from blog.models import CategoryModel
from blog.models import ArticleModel
# Register your models here.
admin.site.register(CategoryModel)

class ArticleAdmin(admin.ModelAdmin):
    search_fields=("title", "content")
    list_display=(
        "title", "created_date", "edited_date"
    )

admin.site.register(ArticleModel, ArticleAdmin)