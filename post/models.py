"""Models of post app"""

from enum import unique
from django.db import models
from django.contrib.auth import get_user_model


POST_STATUS = (
    ("draft", "Draft"),
    ("publish", "Publish"),
)

User = get_user_model()


class LikeDate(models.Model):
    """Date of like"""

    date = models.DateField(
        auto_now_add=True,
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.date)

    class Meta:
        """Metainformation about LikeDate model"""

        unique_together = ('user', 'post',)


# TODO: Union with LikeDate
class DislikeDate(models.Model):
    """Dates of dislikes"""

    date = models.DateField(
        auto_now_add=True
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.date)

    class Meta:
        """Metainformation about DislikeDate model"""

        unique_together = ('user', 'post',)


class Post(models.Model):
    """Blog's post"""

    title = models.CharField(
        max_length=255,
        db_index=True,
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
    )

    content = models.TextField(
        db_index=True,
    )

    published_time = models.DateTimeField(
        auto_now_add=True,
    )

    updated_time = models.DateTimeField(
        auto_now=True,
    )

    status = models.CharField(
        max_length=20,
        choices=POST_STATUS,
        default="publish",
    )

    likes = models.PositiveIntegerField(
        default=0,
    )

    dislikes = models.PositiveIntegerField(
        default=0,
    )

    liked_authors = models.ManyToManyField(
        User,
        related_name='liked_authors',
        blank=True,
    )

    disliked_authors = models.ManyToManyField(
        User,
        related_name='disliked_authors',
        blank=True,
    )

    def __str__(self):
        return str(self.title) + " (" + str(self.author) + ")"

    class Meta:
        """Metainformation about Post model"""

        unique_together = ('title', 'author',)

        ordering = ('-published_time',)
