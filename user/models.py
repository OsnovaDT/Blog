"""Models of user app"""

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class UserLastRequest(models.Model):
    """Last request for the specified user"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    last_request = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return str(self.user) + " (" + str(self.last_request) + ")"
