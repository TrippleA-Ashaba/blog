from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, "blog/home.html")


def tutorial_view(request):
    return render(request, "blog/posts.html", {"category": "Tutorials"})


def tales_view(request):
    return render(request, "blog/posts.html", {"category": "Tales"})


def single_post_view(request):
    return render(request, "blog/single_post.html")


def about_view(request):
    return render(request, "blog/about.html")
