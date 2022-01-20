"""Views of accounts app"""

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class SignUp(CreateView):
    """User's signup"""

    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('post:all_posts')
