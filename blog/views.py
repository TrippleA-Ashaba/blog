import datetime
import logging

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from taggit.models import Tag
from .forms import CommentForm
from .models import Comment, Post

logger = logging.getLogger(__name__)


def home_view(request):
    # logger.info(f"{logger}  Homepage accessed at {datetime.datetime.now()}")
    posts = Post.objects.filter(status="p")
    num_of_posts = posts.count()
    tags = Tag.objects.all()[:10]
    return render(
        request, "blog/home.html", {"posts": posts, "num": num_of_posts, "tags": tags}
    )


def tutorial_view(request):
    posts = Post.objects.filter(category="t")
    tags = Tag.objects.all()[:10]

    return render(
        request,
        "blog/posts.html",
        {
            "title": "| Tutorials",
            "category": "Tutorials",
            "posts": posts,
            "tags": tags,
        },
    )


def single_post_view(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post)
    num_of_comments = comments.count()
    tags = Tag.objects.all()[:10]

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())

    return render(
        request,
        "blog/single_post.html",
        {"post": post, "comments": comments, "num": num_of_comments, "tags": tags},
    )


def about_view(request):
    return render(request, "blog/about.html", {"title": "| About"})
