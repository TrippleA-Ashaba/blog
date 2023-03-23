from django.urls import path

from blog.views import (
    about_view,
    home_view,
    search_tags_view,
    search_view,
    single_post_view,
    tutorial_view,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("tutorials/", tutorial_view, name="tutorials"),
    path("post/<slug:slug>/", single_post_view, name="post_detail"),
    path("about/", about_view, name="about"),
    path("search/", search_view, name="search"),
    path("tag/", search_tags_view, name="search_tag"),
]
