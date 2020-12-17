# views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated


@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def api_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_posts_detail(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        if request.user == post.author:
            serializer = PostSerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)
    elif request.method == 'DELETE':
        if request.user == post.author:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)

#urls.py

from django.urls import path
from .views import api_posts,  api_posts_detail #  импортируйте нужную функцию
from rest_framework.authtoken import views

urlpatterns = [
    path('api/v1/posts/', api_posts),
    path('api/v1/posts/<int:id>/', api_posts_detail)
]

urlpatterns += [
    path('api/v1/api-token-auth/', views.obtain_auth_token)
]

#serializers.py

from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        model = Post
        read_only_fields = ['author']