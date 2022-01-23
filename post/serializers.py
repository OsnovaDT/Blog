"""DRF serializers of post app"""

from rest_framework.serializers import ModelSerializer

from post.models import LikeDates, DislikeDates


class PostLikeDatesSerializer(ModelSerializer):
    """Serializer for likes on a post"""

    class Meta:
        """Metainformation about the serializer"""

        model = LikeDates
        fields = ('user_id', 'post_id', 'like_date',)


class PostDislikeDatesSerializer(ModelSerializer):
    """Serializer for dislikes on a post"""

    class Meta:
        """Metainformation about the serializer"""

        model = DislikeDates
        fields = ('user_id', 'post_id', 'dislike_date',)
