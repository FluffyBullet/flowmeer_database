from flowmeer_db.permissions import IsOwnerOrReadOnly
from django.http import Http404
from rest_framework import status 
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

# Create your views here.
class ListProfile(generics.ListAPIView):
    """
    Call all profiles for view with the class
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer   

class DetailProfile(generics.RetrieveUpdateAPIView):
    """
    Fetch profile data for owner to update if requested/required.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer 