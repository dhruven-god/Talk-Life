from django.urls import path,include
from . import views



urlpatterns = [
    path("", views.PostListView.as_view(),name="post-list-page"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(),name="post-detail-page"),
    path("write/", views.WriteView.as_view(),name="write-post"),
    path("posts/<slug:slug>/delete", views.DeletePostView.as_view(),name="delete"),
]