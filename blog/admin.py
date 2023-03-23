from django.contrib import admin

from accounts.models import CustomUser

from .models import Comment, Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "category",
        "date_published",
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
