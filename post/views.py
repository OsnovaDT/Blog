"""Views of post app"""

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from post.models import Post


class PostListView(ListView):
    """Posts's list"""

    model = Post
    paginate_by = 10
    template_name='post/all_posts.html'
    context_object_name = 'posts'


class CreatePostView(LoginRequiredMixin, CreateView):
    """View for creating post"""

    model = Post
    template_name = 'post/create_post.html'
    fields = ('title', 'content', 'author', 'slug', 'status')
