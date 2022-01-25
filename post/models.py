"""Models of post app"""

from django.db import models
from django.contrib.auth import get_user_model


POST_STATUS = (
    ("draft", "Draft"),
    ("publish", "Publish"),
)

User = get_user_model()


class LikeDates(models.Model):
    """Dates of likes"""

    like_date = models.DateField(
        auto_now_add=True,
    )

    user_id = models.PositiveIntegerField(
        editable=False,
    )

    post_id = models.PositiveIntegerField(
        editable=False,
    )

    def __str__(self):
        return str(self.like_date)

    class Meta:
        """Metainformation about LikeDates model"""

        unique_together = (
            'user_id', 'post_id',
        )


class DislikeDates(models.Model):
    """Dates of dislikes"""

    dislike_date = models.DateField(
        auto_now_add=True
    )

    user_id = models.PositiveIntegerField(
        editable=False,
    )

    post_id = models.PositiveIntegerField(
        editable=False,
    )

    def __str__(self):
        return str(self.dislike_date)

    class Meta:
        """Metainformation about DislikeDates model"""

        unique_together = (
            'user_id', 'post_id',
        )


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
        null=True,
    )

    disliked_authors = models.ManyToManyField(
        User,
        related_name='disliked_authors',
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.title) + " (" + str(self.author) + ")"

    class Meta:
        """Metainformation about Post model"""

        unique_together = ('title', 'author',)

        ordering = ('-published_time',)
