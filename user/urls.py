"""Routes of user app"""

from django.urls import path

from user.views import UserDetailView, UserLastLoginApi, UserLastRequestApi


app_name = 'user'

urlpatterns = [
    path(
        '<int:pk>/',
        UserDetailView.as_view(),
        name='detail',
    ),

    # API
    path(
        'api/last_login/',
        UserLastLoginApi.as_view(),
        name='api_user_last_login',
    ),

    path(
        'api/last_request/',
        UserLastRequestApi.as_view(),
        name='api_user_last_request',
    ),
]
