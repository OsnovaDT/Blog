"""Models of post app"""

from django.db import models
from django.contrib.auth import get_user_model


POST_STATUS = (
    ("draft", "Draft"),
    ("publish", "Publish"),
)

User = get_user_model()


class LikeDates(models.Model):
    """Post's likes dates"""

    user_id = models.PositiveIntegerField()
    post_id = models.PositiveIntegerField()
    like_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "post: " + str(self.post_id) + " | user: " + str(self.user_id)

    class Meta:
        """Metainformation about the model"""

        unique_together = ('user_id', 'post_id')


class DislikeDates(models.Model):
    """Post's dislikes dates"""

    user_id = models.PositiveIntegerField()
    post_id = models.PositiveIntegerField()
    dislike_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "post: " + str(self.post_id) + " | user: " + str(self.user_id)

    class Meta:
        """Metainformation about the model"""

        unique_together = ('user_id', 'post_id')


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
        default="draft",
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
        return str(self.title)[:40] + "... (" + str(self.author) + ")"

    class Meta:
        """Metainformation about the model"""

        unique_together = ('title', 'author')
        ordering = ['-published_time']
