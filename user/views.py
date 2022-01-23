"""Views of user app"""

from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView

from user.serializers import UserLastLoginSerializer


class UserDetailView(DetailView):
    """View for user's detail page"""

    model = User
    template_name = 'user/detail.html'


class UserLastLoginApi(ListAPIView):
    """Api for user last login"""

    queryset = User.objects.all()
    serializer_class = UserLastLoginSerializer
