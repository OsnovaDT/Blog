"""Routes of post app"""

from django.urls import path
from django.views.generic.base import TemplateView


app_name = 'post'

urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name='post/all_posts.html'),
        name='all_posts'
    ),
]
