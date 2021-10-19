from django.shortcuts import render
from rest_framework import generics

from .models import Place
from .serializers import PlaceSerializer



class PlaceList(generics.ListCreateAPIView):
    serializers = PlaceSerializer

    def get_queryset(self):
        return Place.objects.filter(owner_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
