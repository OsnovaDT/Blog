"""Views of post app"""

from datetime import datetime
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
from rest_framework.generics import ListAPIView

from post.serializers import (
    PostLikeDatesSerializer, PostDislikeDatesSerializer
)
from post.models import Post, LikeDate, DislikeDates
from blog.views import add_user_id_to_request


class PostLikeDatesApi(ListAPIView):
    """Api with PostLikeDatesSerializer serializer"""

    serializer_class = PostLikeDatesSerializer

    def get_queryset(self):
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')

        return LikeDate.objects.filter(
            date__range=(date_from, date_to),
        )


class PostDislikeDatesApi(ListAPIView):
    """Api with PostDislikeDatesSerializer serializer"""

    serializer_class = PostDislikeDatesSerializer

    def get_queryset(self):
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')

        return DislikeDates.objects.filter(
            date__range=(date_from, date_to),
        )


class PostListView(ListView):
    """Posts's list"""

    model = Post

    paginate_by = 10

    template_name = 'post/all.html'

    context_object_name = 'posts'


class PostCreateView(LoginRequiredMixin, CreateView):
    """View for creating post"""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        add_user_id_to_request(self.request)

        return context

    model = Post

    template_name = 'post/create.html'

    success_url = reverse_lazy('post:all')

    fields = (
        'title', 'content', 'author', 'status',
    )


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

    is_user_liked_this_post = False
    is_user_disliked_this_post = False

    post = get_post_from_request(request)
    user = get_user_from_request(request)

    if user and post:
        is_user_liked_this_post = user in post.liked_authors.all()
        is_user_disliked_this_post = user in post.disliked_authors.all()

    return HttpResponse(
        dumps({
            'is_user_liked_this_post': is_user_liked_this_post,
            'is_user_disliked_this_post': is_user_disliked_this_post,
        })
    )


# TODO: Refactoring
@csrf_exempt
@login_required
def process_click_of_like(request: WSGIRequest) -> HttpResponse:
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

                if LikeDate.objects.filter(user=user, post=post).exists():
                    like_date = LikeDate.objects.get(
                        user=user, post=post
                    )
                    like_date.delete()

            # If user change dislike to like
            elif user in post.disliked_authors.all():
                post.likes += 1
                post.dislikes -= 1

                post.liked_authors.add(user)
                post.disliked_authors.remove(user)

                if LikeDate.objects.filter(user=user, post=post).exists():
                    like_date = LikeDate.objects.get(
                        user=user, post=post
                    )
                    like_date.date = datetime.now()
                else:
                    like_date = LikeDate.objects.create(
                        user=user, post=post, date=datetime.now(),
                    )
                like_date.save()

                if DislikeDates.objects.filter(user=user, post=post).exists():
                    dislike_date = DislikeDates.objects.get(
                        user=user, post=post
                    )
                    dislike_date.delete()

                is_user_liked_this_post = True

            # If user add like
            else:
                post.likes += 1
                post.liked_authors.add(user)

                like_date = LikeDate.objects.create(
                    user=user, post=post, date=datetime.now(),
                )
                like_date.save()

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


# TODO: Refactoring
@csrf_exempt
@login_required
def process_click_of_dislike(request: WSGIRequest) -> HttpResponse:
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

                if DislikeDates.objects.filter(user=user, post=post).exists():
                    dislike_date = DislikeDates.objects.get(
                        user=user, post=post
                    )
                    dislike_date.delete()

            # If user change like to dislike
            elif user in post.liked_authors.all():
                post.dislikes += 1
                post.likes -= 1

                post.disliked_authors.add(user)
                post.liked_authors.remove(user)

                is_user_disliked_this_post = True

                if DislikeDates.objects.filter(user=user, post=post).exists():
                    dislike_date = DislikeDates.objects.get(
                        user=user, post=post
                    )
                    dislike_date.date = datetime.now()
                else:
                    dislike_date = DislikeDates.objects.create(
                        user=user, post=post, date=datetime.now(),
                    )
                dislike_date.save()

                if LikeDate.objects.filter(user=user, post=post).exists():
                    like_date = LikeDate.objects.get(
                        user=user, post=post
                    )
                    like_date.delete()

            # If user add dislike
            else:
                post.dislikes += 1
                post.disliked_authors.add(user)

                is_user_disliked_this_post = True

                dislike_date = DislikeDates.objects.create(
                    user=user, post=post, date=datetime.now(),
                )
                dislike_date.save()

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
