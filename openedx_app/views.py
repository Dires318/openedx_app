"""
Views for the rest api.
"""
from rest_framework import generics
from .serializers import Greating, GreatingSerializer

class GreatingList(generics.ListCreateAPIView):
    serializer_class = GreatingSerializer
    queryset = Greating.objects.all()

class GreatingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GreatingSerializer
    queryset = Greating.objects.all()
