"""DRF serializers of user app"""

from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserLastLoginSerializer(ModelSerializer):
    """Serializer for User model"""

    class Meta:
        """Metainformation for the serializer"""

        model = User
        fields = ('id', 'username', 'last_login')
