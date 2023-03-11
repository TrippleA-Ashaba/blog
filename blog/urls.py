from django.urls import path

from .views import home_view, tutorial_view

urlpatterns = [
    path("", home_view, name="home"),
    path("tutorial/", tutorial_view, name="tutorial"),
]
