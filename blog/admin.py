from django.contrib import admin
from .models import Post, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "date_published",
        # "category",
        # "status",
    )
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "content", "post", "date_published")
    list_filter = ("post", "date_published")
    search_fields = ("name", "content")
