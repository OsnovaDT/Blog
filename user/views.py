from django.views.generic.detail import DetailView
from django.contrib.auth.models import User


class UserDetailView(DetailView):
    """View for user's detail page"""

    model = User
    template_name = 'user/detail.html'
