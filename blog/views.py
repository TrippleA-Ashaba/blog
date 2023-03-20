import logging

from django.http import HttpResponse
from django.shortcuts import render
import datetime
from .models import Post

logger = logging.getLogger(__name__)


def home_view(request):
    # logger.info(f"{logger}  Homepage accessed at {datetime.datetime.now()}")
    posts = Post.objects.all()
    return render(request, "blog/home.html", {"posts": posts})


def tutorial_view(request):
    return render(
        request, "blog/posts.html", {"title": "| Tutorials", "category": "Tutorials"}
    )


def tales_view(request):
    return render(request, "blog/posts.html", {"title": "| Tales", "category": "Tales"})


def single_post_view(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, "blog/single_post.html", {"post": post})


def about_view(request):
    return render(request, "blog/about.html", {"title": "| About"})
