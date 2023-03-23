from django.urls import path

from .views import home_view, tutorial_view, single_post_view, about_view

urlpatterns = [
    path("", home_view, name="home"),
    path("tutorials/", tutorial_view, name="tutorials"),
    path("post/<slug:slug>/", single_post_view, name="post_detail"),
    path("about/", about_view, name="about"),
]
