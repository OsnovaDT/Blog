"""Tests for models in post app"""

from django.test import TestCase, tag
from django.contrib.auth import get_user_model

from post.models import Post, LikeDates
from post.tests.mixins import COMMON_MIXINS, TestModelUniqueTogether


User = get_user_model()


@tag('post_model')
class LikeDatesTests(TestCase, *COMMON_MIXINS, TestModelUniqueTogether):
    """Tests for LikeDates model"""

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(username='test_user',)

        test_user_2 = User.objects.create(username='test_user_2',)

        test_post = Post.objects.create(
            author=test_user,
            title='Test title',
            content='Test content',
        )

        cls.like_date = LikeDates.objects.create(
            user=test_user_2, post=test_post,
        )

        cls.field_and_verbose_name = {
            'date': 'date',
            'user': 'user',
            'post': 'post',
        }

        cls.auto_now_add_fields = ('date',)

        cls.model_unique_together = ('user', 'post',)

        cls.model_verbose_name = 'like dates'

        cls.model_verbose_name_plural = 'like datess'

    def test_verbose_name(self):
        """Test verbose_name field"""

        super().test_verbose_name(LikeDates)

    def test_auto_now_add(self):
        """Test auto_now_add field"""

        super().test_auto_now_add(LikeDates)

    def test_object_string_display(self):
        """Test object display"""

        super().test_object_string_display(
            self.like_date, str(self.like_date.date)
        )

    def test_unique_together_of_model(self):
        """Test unique_together field for the model"""

        super().test_unique_together_of_model(LikeDates)

    def test_verbose_name_of_model(self):
        """Test verbose_name field for the model"""

        super().test_verbose_name_of_model(LikeDates)

    def test_verbose_name_plural_of_model(self):
        """Test verbose_name_plural field for the model"""

        super().test_verbose_name_plural_of_model(LikeDates)
