from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from api.models import Post, Comment, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(
        source='author.username',
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date', 'group', )
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(
        source='author.username',
    )

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created', )
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', )
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        read_only=True,
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        fields = ('user', 'following', )
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following'],
                message='You cant follow someone twice',
            )
        ]

    def validate(self, data):
        """
        Exclude sef-follow
        """
        if self.context['request'].user == data.get('following'):
            raise serializers.ValidationError("You cant follow yourself")
        return data
