"""Routes of post app"""

from django.urls import path

from post.views import PostListView, CreatePostView


app_name = 'post'

urlpatterns = [
    path(
        'all/',
        PostListView.as_view(),
        name='all_posts'
    ),
    path(
        'create/',
        CreatePostView.as_view(),
        name='create',
    )
]
