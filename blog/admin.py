from django.contrib import admin
from blog.models import CategoryModel
from blog.models import ArticleModel
from blog.models import CommentModel
from blog.models import ContactModel
# Register your models here.
admin.site.register(CategoryModel)

@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    search_fields=("title", "content")
    list_display=(
        "title", "created_date", "edited_date"
    )

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display=(
        "author", "created_date", "edited_date"
    )
    search_fields=('author__username',)


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display=(
        "email", "created_date"
    )
    search_fields=('email',)
