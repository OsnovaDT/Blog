"""DRF serializers of post app"""

from rest_framework.serializers import ModelSerializer

from post.models import LikeDates, DislikeDates


class PostLikeDatesSerializer(ModelSerializer):
    """Serializer for LikeDates model"""

    class Meta:
        """Metainformation about PostLikeDatesSerializer serializer"""

        model = LikeDates

        fields = (
            'like_date', 'user_id', 'post_id',
        )


class PostDislikeDatesSerializer(ModelSerializer):
    """Serializer for DislikeDates model"""

    class Meta:
        """Metainformation about PostDislikeDatesSerializer serializer"""

        model = DislikeDates

        fields = (
            'dislike_date', 'user_id', 'post_id',
        )
