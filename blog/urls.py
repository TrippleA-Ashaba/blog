from django.urls import path

from blog.views import (
    # about_view,
    # home_view,
    search_tags_view,
    search_view,
    single_post_view,
    # tutorial_view,
    HomeView,
    TutorialPostsView,
    # PostDetailView,
    AboutView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("tutorials/", TutorialPostsView.as_view(), name="tutorials"),
    path("post/<slug:slug>/", single_post_view, name="post_detail"),
    path("about/", AboutView.as_view(), name="about"),
    path("search/", search_view, name="search"),
    path("tag/", search_tags_view, name="search_tag"),
    # path("home_test/", PostDetailView.as_view(), name="home_test"),
]
