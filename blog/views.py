import logging

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from taggit.models import Tag

from blog.forms import CommentForm
from blog.models import Comment, Post

logger = logging.getLogger(__name__)

# Constants
NUM_OF_POSTS = Post.objects.filter(status="p").count()
NUM_OF_TUTORIAL_POSTS = Post.objects.filter(status="p", category="t").count()
TAGS = Tag.objects.all()
PAGES = 10


# Home page view
class HomeView(ListView):
    """Returns a list of all the posts and renders them to home.html"""

    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    extra_context = {
        "num_of_posts": NUM_OF_POSTS,
        "num_of_tutorial_posts": NUM_OF_TUTORIAL_POSTS,
        "tags": TAGS,
    }
    paginate_by = PAGES

    def get_queryset(self):
        return Post.objects.prefetch_related("tags").filter(status="p")


# Tutorial view
class TutorialPostsView(ListView):
    """Returns a list of all the tutorial posts and renders them to post.html"""

    model = Post
    template_name = "blog/posts.html"
    context_object_name = "posts"
    extra_context = {
        "title": "| Tutorials",
        "num_of_posts": NUM_OF_POSTS,
        "num_of_tutorial_posts": NUM_OF_TUTORIAL_POSTS,
        "tags": TAGS,
    }
    paginate_by = PAGES

    def get_queryset(self):
        return Post.objects.prefetch_related("tags").filter(status="p", category="t")


# Detailed view of a particular post
def single_post_view(request, slug):
    """Returns a single post view for a given post slug"""

    # get the current post
    post = Post.objects.get(slug=slug)

    # get the last five posts of similar category
    recommended_posts = Post.objects.filter(status="p", category=post.category).exclude(
        title=post.title
    )[:5]

    # get the comments of the post
    comments = Comment.objects.filter(post=post)
    num_of_comments = comments.count()

    # Handle comments from users and save them in the database
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
            "tags": TAGS,
            "posts": recommended_posts,
            "num_of_comments": num_of_comments,
            "num_of_posts": NUM_OF_POSTS,
            "num_of_tutorial_posts": NUM_OF_TUTORIAL_POSTS,
        },
    )


def about_view(request):
    return render(request, "blog/about.html", {"title": "| About"})


def search_view(request):
    tags = Tag.objects.all()

    query = request.GET.get("q")
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query)
            | Q(content__icontains=query)
            | Q(tags__name__icontains=query)
        ).distinct()

    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/search_results.html",
        {"title": "search results", "search": query, "posts": page_obj, "tags": tags},
    )


def search_tags_view(request):
    tags = Tag.objects.all()
    query = request.GET.get("q")
    if query:
        posts = Post.objects.filter(Q(tags__name__icontains=query)).distinct()

    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/posts.html",
        {"title": "search results", "category": query, "posts": page_obj, "tags": tags},
    )
