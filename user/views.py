"""Views of user app"""

from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView

from user.serializers import UserLastLoginSerializer
from post.models import Post


class UserDetailView(DetailView):
    """View for user's detail page"""

    model = User
    template_name = 'user/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posts'] = Post.objects.filter(
            author=self.object, status='publish'
        )

        context['drafts'] = Post.objects.filter(
            author=self.object, status='draft'
        )

        return context


class UserLastLoginApi(ListAPIView):
    """Api for user last login"""

    queryset = User.objects.all()
    serializer_class = UserLastLoginSerializer
