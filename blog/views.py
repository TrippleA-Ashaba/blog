import logging

from django.http import HttpResponse
from django.shortcuts import render
import datetime

logger = logging.getLogger(__name__)


def home_view(request):
    logger.warning("Homepage accessed")
    logger.warning(__name__)
    return render(request, "blog/home.html")


def tutorial_view(request):
    return render(
        request, "blog/posts.html", {"title": "| Tutorials", "category": "Tutorials"}
    )


def tales_view(request):
    return render(request, "blog/posts.html", {"title": "| Tales", "category": "Tales"})


def single_post_view(request):
    return render(request, "blog/single_post.html")


def about_view(request):
    return render(request, "blog/about.html", {"title": "| About"})
