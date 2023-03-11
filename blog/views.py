from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request):
    return render(request, "blog/index.html")


def tutorial_view(request):
    return render(request, "blog/tutorial.html")


def tales_view(request):
    return render(request, "blog/tutorial.html")


def single_post_view(request):
    return render(request, "blog/single_post.html")


def about_view(request):
    return render(request, "blog/about.html")
