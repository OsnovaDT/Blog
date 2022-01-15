"""Registered models"""

from django.contrib import admin
from post.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin panel for Post model"""

    list_display = (
        'title', 'author', 'status',
        'published_time', 'updated_time',
    )
    list_filter = ('published_time', 'status',)
