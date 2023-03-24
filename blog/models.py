from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

from accounts.models import CustomUser

STATUS_CHOICES = [("d", "Draft"), ("p", "Published")]
CATEGORY_CHOICES = [("t", "Tutorial"), ("o", "Other")]


# POST model
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        null=False,
        unique=True,
    )
    image = models.ImageField(null=True, blank=True, upload_to="covers")
    content = RichTextUploadingField()
    tags = TaggableManager()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_published = models.DateTimeField()
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default="d",
    )
    category = models.CharField(
        max_length=1,
        choices=CATEGORY_CHOICES,
        default="o",
    )

    class Meta:
        ordering = ("-date_published",)

    def __str__(self) -> str:
        return self.title[:50]

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})


# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_published",)

    def __str__(self) -> str:
        return f"Comment {self.content} by {self.name}"
