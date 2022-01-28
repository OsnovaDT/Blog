"""Registered models of user app"""

from django.contrib import admin

from user.models import UserLastRequest


@admin.register(UserLastRequest)
class UserLastRequestAdmin(admin.ModelAdmin):
    """Admin panel for UserLastRequest model"""

    list_display = ('user', 'last_request',)
