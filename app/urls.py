from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("blog/", views.blog, name="blog"),
    path("blog/<int:id>/", views.blog_details, name="blog_details"),
    path("change_lang", views.change_lang, name="change_lang"),
]
