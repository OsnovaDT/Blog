"""DRF serializers of post app"""

from rest_framework.serializers import ModelSerializer

from post.models import LikeDates, DislikeDates


class PostLikeDatesSerializer(ModelSerializer):
    """Serializer for LikeDates model"""

    class Meta:
        """Metainformation about PostLikeDatesSerializer serializer"""

        model = LikeDates

        fields = (
            'date', 'user', 'post',
        )


class PostDislikeDatesSerializer(ModelSerializer):
    """Serializer for DislikeDates model"""

    class Meta:
        """Metainformation about PostDislikeDatesSerializer serializer"""

        model = DislikeDates

        fields = (
            'date', 'user', 'post',
        )
