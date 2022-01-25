"""Registered models of post app"""

from django.contrib import admin

from post.models import Post, LikeDates, DislikeDates


class LikeDatesAdmin(admin.ModelAdmin):
    """Admin panel for LikeDates model"""

    list_display = (
        'date', 'user', 'post',
    )


class DislikeDatesAdmin(admin.ModelAdmin):
    """Admin panel for DislikeDates model"""

    list_display = (
        'date', 'user', 'post',
    )


class PostAdmin(admin.ModelAdmin):
    """Admin panel for Post model"""

    list_display = (
        'title', 'author', 'status',
        'published_time', 'updated_time',
    )

    list_filter = (
        'published_time', 'status',
    )


MODEL_WITH_ADMIN_MODEL = {
    LikeDates: LikeDatesAdmin,
    DislikeDates: DislikeDatesAdmin,
    Post: PostAdmin,
}

for model, admin_model in MODEL_WITH_ADMIN_MODEL.items():
    admin.site.register(model, admin_model)
