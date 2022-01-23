"""Routes of accounts app"""

from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView,
    PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetView,
    PasswordResetDoneView,
)

from accounts.views import SignUp


app_name = 'accounts'

urlpatterns = [
    # Signup
    path('signup/', SignUp.as_view(), name='signup'),

    # Login and logout
    path(
        'login/',
        LoginView.as_view(template_name='accounts/login.html'),
        name='login'
    ),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Password change
    path(
        'change_password/',
        PasswordChangeView.as_view(
            template_name='accounts/change_password.html',
            success_url=reverse_lazy('post:all_posts'),
        ),
        name='password_change'
    ),

    # Password reset
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='accounts/password_reset/password_reset.html',
            subject_template_name=\
                'accounts/password_reset/message_subject.txt',
            email_template_name=\
                'accounts/password_reset/message_body.html',
            success_url=reverse_lazy('accounts:message_sent'),
        ),
        name="password_reset"
    ),

    path(
        'password_reset/message_sent/',
        PasswordResetDoneView.as_view(
            template_name='accounts/password_reset/message_sent.html',
            extra_context={'is_message_sent': True},
        ),
        name="message_sent"
    ),

    path(
        'password_reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset/set_new_password.html',
            success_url=reverse_lazy('accounts:password_successfully_reset'),
        ),
        name="set_new_password"
    ),

    path(
        'password_reset/done/',
        PasswordResetCompleteView.as_view(
            template_name=\
                'accounts/password_reset/password_successfully_reset.html',
        ),
        name='password_successfully_reset'
    ),
]
