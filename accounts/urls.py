"""Routes of accounts app"""

from django.urls import path

from accounts.views import SignUp


app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
]
