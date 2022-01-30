"""Tests for models in user app"""

from django.test import TestCase, tag
from django.contrib.auth import get_user_model

from blog.tests_mixins import COMMON_MIXINS, TestAutoNowMixin
from user.models import UserLastRequest


User = get_user_model()

@tag('user_model')
class UserLastRequestTests(TestCase, *COMMON_MIXINS, TestAutoNowMixin):
    """Tests for Post model"""

    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create(username='test_user',)

        cls.test_last_request = UserLastRequest.objects.create(
            user=cls.test_user
        )

        cls.field_and_verbose_name = {
            'user': 'user',
            'last_request': 'last request',
        }

        cls.auto_now_fields = ('last_request',)

        cls.model_verbose_name = 'user last request'

        cls.model_verbose_name_plural = 'user last requests'

    def test_verbose_name(self):
        """Test verbose_name field"""

        super().test_verbose_name(UserLastRequest)

    def test_auto_now(self):
        """Test auto_now field"""

        super().test_auto_now(UserLastRequest)

    def test_object_string_display(self):
        """Test object display"""

        super().test_object_string_display(
            self.test_last_request,
            str(self.test_user) + \
                " (" + str(self.test_last_request.last_request) + ")"
        )

    def test_verbose_name_of_model(self):
        """Test verbose_name field for the model"""

        super().test_verbose_name_of_model(UserLastRequest)

    def test_verbose_name_plural_of_model(self):
        """Test verbose_name_plural field for the model"""

        super().test_verbose_name_plural_of_model(UserLastRequest)
