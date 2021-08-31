from django.contrib import admin
from blog.models import CategoryModel
from blog.models import ArticleModel
from blog.models import CommentModel
# Register your models here.
admin.site.register(CategoryModel)

class ArticleAdmin(admin.ModelAdmin):
    search_fields=("title", "content")
    list_display=(
        "title", "created_date", "edited_date"
    )

class CommentAdmin(admin.ModelAdmin):
    list_display=(
        "author", "created_date", "edited_date"
    )
    search_fields=('author__username',)

admin.site.register(CommentModel, CommentAdmin)
admin.site.register(ArticleModel, ArticleAdmin)