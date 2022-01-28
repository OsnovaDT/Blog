"""DRF serializers of user app"""

from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from user.models import UserLastRequest


class UserLastLoginSerializer(ModelSerializer):
    """Serializer for User model"""

    class Meta:
        """Metainformation for the serializer"""

        model = User
        fields = ('id', 'username', 'last_login')


class UserLastRequestSerializer(ModelSerializer):
    """Serializer for UserLastRequest model"""

    class Meta:
        """Metainformation for the serializer"""

        model = UserLastRequest
        fields = ('user', 'last_request')
