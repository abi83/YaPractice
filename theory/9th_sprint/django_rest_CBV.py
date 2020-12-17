from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer


class APIPost(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIPostDetail(APIView):
    def get(self, request, id):
        post = Post.objects.get(pk=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, id):
        post = Post.objects.get(pk=id)
        if request.user == post.author:
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def patch(self, request, id):
        post = Post.objects.get(pk=id)
        if request.user == post.author:
            serializer = PostSerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, id):
        post = Post.objects.get(pk=id)
        if request.user == post.author:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)
