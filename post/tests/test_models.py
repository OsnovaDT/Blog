"""Tests for models in post app"""

from django.test import TestCase, tag
from django.contrib.auth import get_user_model

from post.models import Post, LikeDate, DislikeDate
from post.tests.mixins import (
    COMMON_MIXINS, TestModelUniqueTogether, TestMaxLengthMixin,
    TestDbIndexMixin, TestAutoNowMixin, TestChoicesMixin, TestBlankMixin,
    TestDefaultMixin, TestModelOrdering,
)


User = get_user_model()

POST_STATUS = (
    ("draft", "Draft"),
    ("publish", "Publish"),
)


@tag('post_model')
class LikeDateTests(TestCase, *COMMON_MIXINS, TestModelUniqueTogether):
    """Tests for LikeDate model"""

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(username='test_user',)

        test_user_2 = User.objects.create(username='test_user_2',)

        test_post = Post.objects.create(
            author=test_user,
            title='Test title',
            content='Test content',
        )

        cls.like_date = LikeDate.objects.create(
            user=test_user_2, post=test_post,
        )

        cls.field_and_verbose_name = {
            'date': 'date',
            'user': 'user',
            'post': 'post',
        }

        cls.auto_now_add_fields = ('date',)

        cls.model_unique_together = ('user', 'post',)

        cls.model_verbose_name = 'like date'

        cls.model_verbose_name_plural = 'like dates'

    def test_verbose_name(self):
        """Test verbose_name field"""

        super().test_verbose_name(LikeDate)

    def test_auto_now_add(self):
        """Test auto_now_add field"""

        super().test_auto_now_add(LikeDate)

    def test_object_string_display(self):
        """Test object display"""

        super().test_object_string_display(
            self.like_date, str(self.like_date.date)
        )

    def test_unique_together_of_model(self):
        """Test unique_together field for the model"""

        super().test_unique_together_of_model(LikeDate)

    def test_verbose_name_of_model(self):
        """Test verbose_name field for the model"""

        super().test_verbose_name_of_model(LikeDate)

    def test_verbose_name_plural_of_model(self):
        """Test verbose_name_plural field for the model"""

        super().test_verbose_name_plural_of_model(LikeDate)


@tag('post_model')
class DislikeDateTests(TestCase, *COMMON_MIXINS, TestModelUniqueTogether):
    """Tests for DislikeDate model"""

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(username='test_user',)

        test_user_2 = User.objects.create(username='test_user_2',)

        test_post = Post.objects.create(
            author=test_user,
            title='Test title',
            content='Test content',
        )

        cls.dislike_date = DislikeDate.objects.create(
            user=test_user_2, post=test_post,
        )

        cls.field_and_verbose_name = {
            'date': 'date',
            'user': 'user',
            'post': 'post',
        }

        cls.auto_now_add_fields = ('date',)

        cls.model_unique_together = ('user', 'post',)

        cls.model_verbose_name = 'dislike date'

        cls.model_verbose_name_plural = 'dislike dates'

    def test_verbose_name(self):
        """Test verbose_name field"""

        super().test_verbose_name(DislikeDate)

    def test_auto_now_add(self):
        """Test auto_now_add field"""

        super().test_auto_now_add(DislikeDate)

    def test_object_string_display(self):
        """Test object display"""

        super().test_object_string_display(
            self.dislike_date, str(self.dislike_date.date)
        )

    def test_unique_together_of_model(self):
        """Test unique_together field for the model"""

        super().test_unique_together_of_model(DislikeDate)

    def test_verbose_name_of_model(self):
        """Test verbose_name field for the model"""

        super().test_verbose_name_of_model(DislikeDate)

    def test_verbose_name_plural_of_model(self):
        """Test verbose_name_plural field for the model"""

        super().test_verbose_name_plural_of_model(DislikeDate)


@tag('post_model')
class PostTests(
    TestCase, *COMMON_MIXINS, TestModelUniqueTogether,
    TestMaxLengthMixin, TestDbIndexMixin, TestAutoNowMixin,
    TestChoicesMixin, TestBlankMixin, TestDefaultMixin,
    TestModelOrdering,):
    """Tests for Post model"""

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(username='test_user',)

        cls.test_post = Post.objects.create(
            author=test_user,
            title='Test title',
            content='Test content',
        )

        cls.field_and_verbose_name = {
            'title': 'title',
            'author': 'author',
            'content': 'content',
            'published_time': 'published time',
            'updated_time': 'updated time',
            'status': 'status',
            'likes': 'likes',
            'dislikes': 'dislikes',
            'liked_authors': 'liked authors',
            'disliked_authors': 'disliked authors',
        }

        cls.field_and_max_length = {
            'title': 255,
            'status': 20,
        }

        cls.field_and_choices = {
            'status': POST_STATUS,
        }

        cls.field_and_default = {
            'status': 'publish',
            'likes': 0,
            'dislikes': 0,
        }

        cls.db_index_fields = (
            'title', 'content',
        )

        cls.blank_fields = ('liked_authors', 'disliked_authors',)

        cls.auto_now_add_fields = ('published_time',)

        cls.auto_now_fields = ('updated_time',)

        cls.model_unique_together = ('title', 'author',)

        cls.model_ordering = ('-published_time',)

        cls.model_verbose_name = 'post'

        cls.model_verbose_name_plural = 'posts'

    def test_verbose_name(self):
        """Test verbose_name field"""

        super().test_verbose_name(Post)

    def test_auto_now_add(self):
        """Test auto_now_add field"""

        super().test_auto_now_add(Post)

    def test_auto_now(self):
        """Test auto_now field"""

        super().test_auto_now(Post)

    def test_choices(self):
        """Test choices field"""

        super().test_choices(Post)

    def test_default(self):
        """Test default field"""

        super().test_default(Post)

    def test_blank(self):
        """Test blank field"""

        super().test_blank(Post)

    def test_max_length(self):
        """Test max_length field"""

        super().test_max_length(Post)

    def test_db_index(self):
        """Test db_index field"""

        super().test_db_index(Post)

    def test_object_string_display(self):
        """Test object display"""

        super().test_object_string_display(
            self.test_post,
            str(self.test_post.title) + " (" + str(self.test_post.author) + ")"
        )

    def test_unique_together_of_model(self):
        """Test unique_together field for the model"""

        super().test_unique_together_of_model(Post)

    def test_ordering_of_model(self):
        """Test ordering field for the model"""

        super().test_ordering_of_model(Post)

    def test_verbose_name_of_model(self):
        """Test verbose_name field for the model"""

        super().test_verbose_name_of_model(Post)

    def test_verbose_name_plural_of_model(self):
        """Test verbose_name_plural field for the model"""

        super().test_verbose_name_plural_of_model(Post)
