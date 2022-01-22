"""Views of post app"""

from json import dumps

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponse

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


def get_post_with_user(request):
    """Return post and user objects from request"""

    post_id = request.POST['post_id']
    user_id = request.POST['user_id']

    post = Post.objects.get(id=post_id)
    user = User.objects.get(id=user_id)

    return post, user


@csrf_exempt
@login_required
def check_estimation(request):
    """Check is the post has likes or dislikes from the user"""

    post, user = get_post_with_user(request)

    is_liked = user in post.liked_authors.all()
    is_disliked = user in post.disliked_authors.all()

    return HttpResponse(dumps({
        'is_liked': is_liked,
        'is_disliked': is_disliked,
    }))


@csrf_exempt
@login_required
def like_post(request):
    """Like the post"""

    post, user = get_post_with_user(request)

    # If user delete the like
    if user in post.liked_authors.all():
        post.likes -= 1
        post.liked_authors.remove(user)
        is_liked = False

    # If user change dislike to like
    elif user in post.disliked_authors.all():
        post.likes += 1
        post.dislikes -= 1

        post.liked_authors.add(user)
        post.disliked_authors.remove(user)

        is_liked = True

    # If user likes the post
    else:
        post.likes += 1
        post.liked_authors.add(user)

        is_liked = True

    post.save()

    return HttpResponse(dumps({
        'likes': post.likes,
        'dislikes': post.dislikes,
        'is_liked': is_liked,
    }))

@csrf_exempt
@login_required
def dislike_post(request):
    """Dislike the post"""

    post, user = get_post_with_user(request)

    # If user delete the like
    if user in post.disliked_authors.all():
        post.dislikes -= 1
        post.disliked_authors.remove(user)

        is_disliked = False

    # If user change like to dislike
    elif user in post.liked_authors.all():
        post.dislikes += 1
        post.likes -= 1

        post.disliked_authors.add(user)
        post.liked_authors.remove(user)

        is_disliked = True

    # If user dislikes the post
    else:
        post.dislikes += 1
        post.disliked_authors.add(user)

        is_disliked = True

    post.save()

    return HttpResponse(dumps({
        'likes': post.likes,
        'dislikes': post.dislikes,
        'is_disliked': is_disliked,
    }))
