"""Routes of accounts app"""

from django.urls import path
from django.contrib.auth.views import LoginView

from accounts.views import SignUp


app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path(
        'login/',
        LoginView.as_view(template_name='accounts/login.html'),
        name='login'
    ),
]
