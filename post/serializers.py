"""DRF serializers of post app"""

from rest_framework.serializers import ModelSerializer

from post.models import LikeDate, DislikeDate


class PostLikeDateSerializer(ModelSerializer):
    """Serializer for LikeDate model"""

    class Meta:
        """Metainformation about PostLikeDateSerializer serializer"""

        model = LikeDate

        fields = (
            'date', 'user', 'post',
        )


class PostDislikeDateSerializer(ModelSerializer):
    """Serializer for DislikeDate model"""

    class Meta:
        """Metainformation about PostDislikeDateSerializer serializer"""

        model = DislikeDate

        fields = (
            'date', 'user', 'post',
        )
