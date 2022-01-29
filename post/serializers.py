"""DRF serializers of post app"""

from rest_framework.serializers import ModelSerializer

from post.models import LikeDate, DislikeDates


class PostLikeDatesSerializer(ModelSerializer):
    """Serializer for LikeDate model"""

    class Meta:
        """Metainformation about PostLikeDatesSerializer serializer"""

        model = LikeDate

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
