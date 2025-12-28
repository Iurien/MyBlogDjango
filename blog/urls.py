from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostShareView, AboutView, ContactView
)
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('tag/<slug:tag_slug>/', PostListView.as_view(),
         name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         PostDetailView.as_view(), name='post_detail'),
    path('<int:post_id>/share/', PostShareView.as_view(), name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
