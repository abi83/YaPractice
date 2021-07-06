from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import Post
from posts.permissions import IsCommentOrPostOwner
from posts.serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    Basic Post API with very common behavior.
    PUT, PATCH, DELETE methods only for Post owner
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsCommentOrPostOwner)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Basic Comments API with very common behavior.
    PUT, PATCH, DELETE methods only for Post owner
    """
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsCommentOrPostOwner)

    def get_queryset(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=int(self.kwargs.get('post_id')))
        return post.comments.all()

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
