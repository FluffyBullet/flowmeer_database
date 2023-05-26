from django.shortcuts import render
from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from flowmeer_db.permissions import IsOwnerOrReadOnly

# Create your views here.

class ListPost(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
        post = Post.objects.all()
        authenticated = PostSerializer(post, many=True, context={'request':request})
        return Response(authenticated.data)
    
    def post(self,request):
        authenticated = PostSerializer(
            data=request.data, context={'request':request}
        )
        if authenticated.is_valid():
            authenticated.save(owner=request.user)
            return Response(authenticated.data, status=status.HTTP_201_CREATED)
        return Response(authenticated.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailPost(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    
    def get_object(self,pk):
        try:
            post = Post.objects.get(pk=pk)
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        post = self.get_object(pk)
        authenticated = PostSerializer(
            post, context={'request':request}
        )
        return Response(authenticated.data)
            
    def put(self, request, pk):
        post = self.get_object(pk)
        authenticated = PostSerializer(
            post, data=request.data, context={'request':request }
        )
        if authenticated.is_valid():
            authenticated.save()
            return Response(authenticated.data)
        return Response(authenticated.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )