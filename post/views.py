from django.db.models import Count
from rest_framework import permissions, filters
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
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
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        votes_count=Count('votes', dinstinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
        'flower_tag',
    ]
    ordering_fields = [
        'votes_count',
        'comments_count',
    ]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)



class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    """
    RUD Function for post, R for all, UD for owner of the post. 
    """

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
