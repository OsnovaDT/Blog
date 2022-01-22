"""Routes of accounts app"""

from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
)

from accounts.views import SignUp


app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path(
        'login/',
        LoginView.as_view(template_name='accounts/login.html'),
        name='login'
    ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path(
        'change_password/',
        PasswordChangeView.as_view(
            template_name='accounts/change_password.html',
            success_url=reverse_lazy('post:all_posts'),
        ),
        name='password_change'
    ),
]
