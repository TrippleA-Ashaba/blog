from django.urls import path

from blog.views import (
    AboutView,
    HomeView,
    SearchResultsView,
    SearchTagsView,
    TutorialPostsView,
    single_post_view,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("tutorials/", TutorialPostsView.as_view(), name="tutorials"),
    path("post/<slug:slug>/", single_post_view, name="post_detail"),
    path("about/", AboutView.as_view(), name="about"),
    path("search/", SearchResultsView.as_view(), name="search"),
    path("tag/", SearchTagsView.as_view(), name="search_tag"),
]
