from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,)

from api.permissions import IsCommentOrPostOwner
from api.serializers import *


class PostViewSet(viewsets.ModelViewSet):
    """
    Basic Post API with very common behavior.
    PUT, PATCH, DELETE methods only for Post owner
    """
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsCommentOrPostOwner)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def get_queryset(self, *args, **kwargs):
        if self.request.query_params.get('group'):
            group = get_object_or_404(
                Group, pk=int(self.request.query_params.get('group')))
            return group.posts.active()
        return Post.objects.active()


class CommentViewSet(viewsets.ModelViewSet):
    """
    Basic Comments API with very common behavior.
    PUT, PATCH, DELETE methods only for Post owner
    """
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsCommentOrPostOwner)

    def get_queryset(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=int(self.kwargs.get('post_id')))
        return post.comments.active()

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ViewSetMixin, generics.ListCreateAPIView):
    """
    Get group list or create new group
    """
    queryset = Group.objects.active()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class FollowViewSet(viewsets.ViewSetMixin, generics.ListCreateAPIView):
    """
    Only for Authenticated users.
    GET request to receive your own follower list
    POST request to follow someone
    """
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self, *args, **kwargs):
        return Follow.objects.filter(following=self.request.user)
