"""Routes of post app"""

from django.urls import path

from post.views import (
    PostListView, CreatePostView, like_post, dislike_post, check_estimation
)


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
    ),
    path(
        'like/',
        like_post,
        name='like',
    ),
    path(
        'dislike/',
        dislike_post,
        name='dislike',
    ),
    path(
        'check_estimation/',
        check_estimation,
        name='check_estimation',
    )
]
