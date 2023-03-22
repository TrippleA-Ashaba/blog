from django.contrib import admin
from .models import Post, Comment
from accounts.models import CustomUser


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "date_published",
        # "category",
    )
    prepopulated_fields = {"slug": ("title",)}
    actions = ["make_published"]

    # Adding actions
    @admin.action(description="Mark selected posts as Published")
    def make_published(self, request, queryset):
        queryset.update(status="p")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "content", "post", "date_published")
    list_filter = ("post", "date_published")
    search_fields = ("name", "content")
