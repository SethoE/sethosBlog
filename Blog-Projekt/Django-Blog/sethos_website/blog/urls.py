from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="home-page"),
    path("posts", views.posts, name="allPosts-page"),
    path("post/<slug:individual_post_slug>", views.individualPost, name="individualPost-page"),
]