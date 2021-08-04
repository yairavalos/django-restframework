from django.contrib.admindocs.views import get_readable_field_data_type
from django.shortcuts import get_object_or_404, render

# REST Framework Libraries.
from rest_framework import status, generics # Introducing Generic Views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

# Models
from .models import PetOwner,Pet
# Serializers
from .serializers import PetOwnersListModelSerializer, PetOwnerModelSerializer, PetListModelSerializer, PetModelSerializer  # PetOwnerSerializer, PetOwnerUpdateSerializer, PetListSerializer, PetUpdateSerializer

# Introducing Generic Views 

class PetOwnersListCreateAPIView(generics.ListCreateAPIView):
    queryset = PetOwner.objects.all().order_by("first_name")
    serializer_class = PetOwnersListModelSerializer

    def get_queryset(self):

        first_name_filter = self.request.GET.get("first_name")
        filters = {}

        if first_name_filter:
            filters["first_name__icontains"] = first_name_filter

        return self.queryset.filter(**filters)

    def get_serializer_class(self):

        serializer_class = self.serializer_class

        if self.request.method == 'POST':
            serializer_class = PetOwnerModelSerializer

        return serializer_class

class PetOwnersRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

        queryset = PetOwner.objects.all()
        serializer_class = PetOwnerModelSerializer


class PetListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pet.objects.all().order_by("type")
    serializer_class = PetListModelSerializer

    def get_queryset(self):

        pet_name_filter = self.request.GET.get("name")
        filters = {}

        if pet_name_filter:
            filters["name__icontains"] = pet_name_filter

        return self.queryset.filter(**filters)

    def get_serializer_class(self):

        serializer_class = self.serializer_class

        if self.request.method == 'POST':
            serializer_class = PetModelSerializer

        return serializer_class

class PetOwnerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = PetOwnerModelSerializer

class PetOwnersCreateAPIView(generics.CreateAPIView): # Genera el Form por default para agregar usuarios
    queryset = PetOwner
    serializer_class = PetOwnerModelSerializer

class PetListAPIView(generics.ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetListModelSerializer

class PetRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetModelSerializer

