"""Routes of post app"""

from django.urls import path

from post.views import (
    PostListView, CreatePostView, PostDetailView,
    like_click_processing, dislike_click_processing, check_post_estimation,
    PostLikeDatesApi, PostDislikeDatesApi,
)


app_name = 'post'

urlpatterns = [
    path(
        '<int:pk>/',
        PostDetailView.as_view(),
        name='detail',
    ),
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
        like_click_processing,
        name='like',
    ),
    path(
        'dislike/',
        dislike_click_processing,
        name='dislike',
    ),
    path(
        'check_estimation/',
        check_post_estimation,
        name='check_estimation',
    ),
    path(
        'api/likes/',
        PostLikeDatesApi.as_view(),
        name='api_likes',
    ),
    path(
        'api/dislikes/',
        PostDislikeDatesApi.as_view(),
        name='api_dislikes',
    ),
]
