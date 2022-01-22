"""Views of post app"""

from json import dumps

from django.views.decorators.csrf import csrf_exempt
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse
from django.urls import reverse_lazy

from post.models import Post


class PostListView(ListView):
    """Posts's list"""

    model = Post
    paginate_by = 10
    template_name = 'post/all_posts.html'
    context_object_name = 'posts'


class CreatePostView(LoginRequiredMixin, CreateView):
    """View for creating post"""

    model = Post
    template_name = 'post/create_post.html'
    fields = ('title', 'content', 'author', 'status')
    success_url = reverse_lazy('post:all_posts')


class PostDetailView(DetailView):
    """Detail view for a post"""

    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'


def get_post_from_request(request: WSGIRequest) -> Post | None:
    """Return POST model's object with id taken from request"""

    post_id = request.POST['post_id']

    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    return post


def get_user_from_request(request: WSGIRequest) -> User | None:
    """Return USER model's object with id taken from request"""

    user_id = request.POST['user_id']

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        user = None

    return user


@csrf_exempt
@login_required
def check_post_estimation(request: WSGIRequest) -> HttpResponse:
    """Check is the post has likes or dislikes from the user"""

    is_user_liked_this_post: False
    is_user_disliked_this_post: False

    post = get_post_from_request(request)
    user = get_user_from_request(request)

    if user and post:
        is_user_liked_this_post = user in post.liked_authors.all()
        is_user_disliked_this_post = user in post.disliked_authors.all()

    return HttpResponse(dumps({
        'is_user_liked_this_post': is_user_liked_this_post,
        'is_user_disliked_this_post': is_user_disliked_this_post,
    }))


@csrf_exempt
@login_required
def like_click_processing(request: WSGIRequest) -> HttpResponse:
    """Processing of clicking on like"""

    is_user_liked_this_post = False

    post = get_post_from_request(request)
    user = get_user_from_request(request)

    if post:
        if user and (user != post.author):
            # If user delete like
            if user in post.liked_authors.all():
                post.likes -= 1
                post.liked_authors.remove(user)

            # If user change dislike to like
            elif user in post.disliked_authors.all():
                post.likes += 1
                post.dislikes -= 1

                post.liked_authors.add(user)
                post.disliked_authors.remove(user)

                is_user_liked_this_post = True

            # If user add like
            else:
                post.likes += 1
                post.liked_authors.add(user)

                is_user_liked_this_post = True

            post.save()

        post_likes = post.likes
        post_dislikes = post.dislikes
    else:
        post_likes = 0
        post_dislikes = 0

    return HttpResponse(
        dumps({
            'likes': post_likes,
            'dislikes': post_dislikes,
            'is_user_liked_this_post': is_user_liked_this_post,
        })
    )


@csrf_exempt
@login_required
def dislike_click_processing(request: WSGIRequest) -> HttpResponse:
    """Processing of clicking on dislike"""

    is_user_disliked_this_post = False

    post = get_post_from_request(request)
    user = get_user_from_request(request)

    if post:
        if user and (user != post.author):
            # If user delete like
            if user in post.disliked_authors.all():
                post.dislikes -= 1
                post.disliked_authors.remove(user)

            # If user change like to dislike
            elif user in post.liked_authors.all():
                post.dislikes += 1
                post.likes -= 1

                post.disliked_authors.add(user)
                post.liked_authors.remove(user)

                is_user_disliked_this_post = True

            # If user add dislike
            else:
                post.dislikes += 1
                post.disliked_authors.add(user)

                is_user_disliked_this_post = True

            post.save()

        post_likes = post.likes
        post_dislikes = post.dislikes
    else:
        post_likes = 0
        post_dislikes = 0

    return HttpResponse(
        dumps({
            'likes': post_likes,
            'dislikes': post_dislikes,
            'is_user_disliked_this_post': is_user_disliked_this_post,
        })
    )
