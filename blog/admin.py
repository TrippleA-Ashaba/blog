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
        "tag_list",
        "date_published",
    )
    prepopulated_fields = {"slug": ("title",)}
    actions = ["make_published"]

    # Adding actions
    @admin.action(description="Mark selected posts as Published")
    def make_published(self, request, queryset):
        queryset.update(status="p")

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")

    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "content", "post", "date_published")
    list_filter = ("post", "date_published")
    search_fields = ("name", "content")
