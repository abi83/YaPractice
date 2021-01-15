from rest_framework import permissions


class IsCommentOrPostOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return obj.author == request.user
        return super(IsCommentOrPostOwner, self
                     ).has_object_permission(request, view, obj)
