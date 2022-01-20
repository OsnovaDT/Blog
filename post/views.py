"""Views of post app"""

from django.views.generic.list import ListView

from post.models import Post


class PostListView(ListView):
    """Posts's list"""

    model = Post
    paginate_by = 10
    template_name='post/all_posts.html'
    context_object_name = 'posts'
