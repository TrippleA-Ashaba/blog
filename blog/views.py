import datetime
import logging

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from taggit.models import Tag

from .forms import CommentForm
from .models import Comment, Post

logger = logging.getLogger(__name__)


def home_view(request):
    # logger.info(f"{logger}  Homepage accessed at {datetime.datetime.now()}")
    posts = Post.objects.filter(status="p")
    tut_posts = Post.objects.filter(status="p", category="t")
    num_of_posts = posts.count()
    tags = Tag.objects.all()[:10]
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/home.html",
        {"posts": page_obj, "num": num_of_posts, "tags": tags, "tuts": tut_posts},
    )


def tutorial_view(request):
    posts = Post.objects.filter(status="p", category="t")
    all_posts = Post.objects.filter(status="p")

    tags = Tag.objects.all()[:10]
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    num_of_posts = all_posts.count()

    return render(
        request,
        "blog/posts.html",
        {
            "title": "| Tutorials",
            "category": "Tutorials",
            "posts": page_obj,
            "tags": tags,
            "num": num_of_posts,
        },
    )


def single_post_view(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.filter(status="p", category=post.category).exclude(
        title=post.title
    )[:5]
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
        {
            "post": post,
            "comments": comments,
            "num": num_of_comments,
            "tags": tags,
            "posts": posts,
        },
    )


def about_view(request):
    return render(request, "blog/about.html", {"title": "| About"})


def search_view(request):
    query = request.GET.get("q")
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query)
            | Q(content__icontains=query)
            | Q(tags__name__icontains=query)
        ).distinct()

        print(
            "========================================= START ============================="
        )
        print(
            "========================================= STOP ============================="
        )
        # return render(
        #     request,
        #     "blog/search_results.html",
        #     {"title": "search results", "search": query, "posts": posts},
        # )
    # return query

    return render(
        request,
        "blog/search_results.html",
        {"title": "search results", "search": query, "posts": posts},
    )
