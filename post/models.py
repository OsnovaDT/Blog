"""Models of post app"""

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


POST_STATUS = (
    ("draft", "Draft"),
    ("publish", "Publish"),
)

User = get_user_model()


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

    slug = models.SlugField(
        max_length=255,
        unique=True,
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

    def __str__(self):
        return str(self.title)[:40] + "... (" + str(self.author) + ")"

    def get_absolute_url(self):
        return reverse_lazy('post:all_posts')

    class Meta:
        """Metainformation about the model"""

        unique_together = ('title', 'author')
        ordering = ['-published_time']
