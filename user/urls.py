"""Routes of user app"""

from django.urls import path

from user.views import UserDetailView


app_name = 'user'

urlpatterns = [
    path(
        '<int:pk>/',
        UserDetailView.as_view(),
        name='detail',
    ),
]
