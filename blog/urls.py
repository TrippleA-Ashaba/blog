from django.urls import path

from .views import home_view, tutorial_view, single_post_view, about_view

urlpatterns = [
    path("", home_view, name="home"),
    path("tutorial/", tutorial_view, name="tutorial"),
    path("tales/", tutorial_view, name="tales"),
    path("post", single_post_view, name="post"),
    path("about/", about_view, name="about"),
]
