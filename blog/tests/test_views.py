"""Tests for views from blog project"""

from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User

from blog.views import add_user_id_to_request


class TestViews(TestCase):
    """Test views"""

    def setUp(self):
        self.factory = RequestFactory()

        self.requests = [
            self.factory.get('/post/all'),
            self.factory.get('/post/1'),
            self.factory.get('/user/1'),
            self.factory.get('/accounts/password_change/'),
            self.factory.get('/post/create/'),

            self.factory.head('/post/all'),
            self.factory.head('/post/1'),
            self.factory.head('/user/1'),
            self.factory.head('/accounts/password_change/'),
            self.factory.head('/post/create/'),
        ]

        self.test_users = (
            User.objects.create(username='test_1'),
            User.objects.create(username='test_2'),
            User.objects.create(username='test_3', email='test_3@gmail.com'),
        )

    def test_add_user_id_to_request(self):
        """Test function add_user_id_to_request"""

        for request in self.requests:
            with self.subTest(f'{request}'):
                for user in self.test_users:
                    request.user = user

                    add_user_id_to_request(request)

                    self.assertIn('user_id', request.POST.keys())
                    self.assertEqual(request.POST['user_id'], request.user.id)
                    self.assertFalse(request.POST._mutable)
