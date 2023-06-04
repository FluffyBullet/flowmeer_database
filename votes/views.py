from rest_framework import generics, permissions
from flowmeer_db.permissions import IsOwnerOrReadOnly
from votes.models import Vote
from votes.serializer import VoteSerializer

class VoteList(generics.ListCreateAPIView):
    '''
    Creates a list of votes and current if user is logged in
    '''

    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VoteDetails(generics.RetrieveDestroyAPIView):
    """
    User can Delete or view by username
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()

    def perform_destroy(self, instance):
        instance.delete()
    