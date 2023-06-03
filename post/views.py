from rest_framework import permissions
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from flowmeer_db.permissions import IsOwnerOrReadOnly

# Create your views here.

class ListPost(generics.ListCreateAPIView):
    """
    Call to action for server to display all post and create if logged in.
    """

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)



class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    """
    RUD Function for post, R for all, UD for owner of the post. 
    """

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
