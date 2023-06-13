from flowmeer_db.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status 
from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

# Create your views here.
class ListProfile(generics.ListAPIView):
    """
    Call all profiles for view with the class
    """
    queryset = Profile.objects.annotate(
        post_cout=Count('owner__post', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    ordering_fields = [
        'post_count',
    ]

class DetailProfile(generics.RetrieveUpdateAPIView):
    """
    Fetch profile data for owner to update if requested/required.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        post_count=Count('owner__post', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer 