"""Routes of post app"""

from django.urls import path

from post.views import (
    PostDetailView, PostListView, PostCreateView,
    process_click_of_like, process_click_of_dislike, check_post_estimation,
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
        name='all',
    ),

    path(
        'create/',
        PostCreateView.as_view(),
        name='create',
    ),

    # Likes and dislikes (Estimation)
    path(
        'like/',
        process_click_of_like,
        name='like',
    ),

    path(
        'dislike/',
        process_click_of_dislike,
        name='dislike',
    ),

    path(
        'check_estimation/',
        check_post_estimation,
        name='check_estimation',
    ),

    # API
    path(
        'api/likes/dates/',
        PostLikeDatesApi.as_view(),
        name='api_likes',
    ),

    path(
        'api/dislikes/dates/',
        PostDislikeDatesApi.as_view(),
        name='api_dislikes',
    ),
]
