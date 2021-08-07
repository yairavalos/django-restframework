from django.contrib.admindocs.views import get_readable_field_data_type
from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend

# REST Framework Libraries.
from rest_framework import status, generics, filters # Introducing Generic Views
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

# Models
from .models import PetDate, PetOwner, Pet
# Serializers
from .serializers import (
    # Pet Owners
    PetDateListModelSerializer,
    PetOwnersListModelSerializer, 
    PetOwnerModelSerializer, 
    # Pets
    PetListModelSerializer, 
    PetModelSerializer,

    # Pet Appointment
    PetDateListModelSerializer,
    PetDateModelSerializer,
    PetDatePetRetrieveModelSerializer,
    PetDatePartialUpdateModelSerializer
    )

# Introducing Generic Views 

class PetOwnersListCreateAPIView(generics.ListCreateAPIView):
    queryset = PetOwner.objects.all().order_by("id")
    serializer_class = PetOwnersListModelSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["first_name"]
    ordering_fields = ["email"]
    permission_classes = [IsAuthenticated]
    #filterset_fields = ["first_name"] 

    def get_queryset(self):

        # due that its a dictionary you can use 
        # python dict methods such as get() or pop() etc.
        first_name_filter = self.request.GET.get("first_name") 
        filters = {}

        # Even when the filter its empty
        # you can create directly over a dict in python
        if first_name_filter:
            filters["first_name__icontains"] = first_name_filter

        return self.queryset.filter(**filters)

    def get_serializer_class(self):

        serializer_class = self.serializer_class

        if self.request.method == 'POST':
            serializer_class = PetOwnerModelSerializer

        return serializer_class


class PetOwnersDatesListCreateAPIView(generics.ListCreateAPIView):

    queryset = PetDate.objects.all()
    serializer_class = PetDateListModelSerializer

    def get_queryset(self):
        owner_id = self.kwargs["pk"]
        filters = {}
        if owner_id:
            filters["pet__owner_id"] = owner_id

        return self.queryset.filter(**filters)


class PetOwnersRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

        queryset = PetOwner.objects.all()
        serializer_class = PetOwnerModelSerializer


class PetListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pet.objects.all().order_by("id")
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

class PetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

        queryset = Pet.objects.all()
        serializer_class = PetModelSerializer

class PetDateListCreateAPIView(generics.ListCreateAPIView):
    queryset = PetDate.objects.all() #.order_by("pet") - punto 6
    serializer_class = PetDateListModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["pet__owner__first_name","pet__name"] #dates given a owner name

    # def get_queryset(self):
    #     date_time_filter = self.request.GET.get("datetime")
    #     filters = {}
    #     if date_time_filter:
    #         filters["datetime__icontains"] = date_time_filter
    #     return self.queryset.filter(**filters)

    def get_serializer_class(self):

        serializer_class = self.serializer_class

        if self.request.method == 'POST':
            serializer_class = PetDateListModelSerializer

        return serializer_class


class PetDateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

        http_method_names = ["get", "patch", "delete"]
        queryset = PetDate.objects.all()
        serializer_class = PetDatePetRetrieveModelSerializer

        def get_serializer_class(self):
            
            serializer_class = self.serializer_class
        
            if self.request.method == "PATCH":
                serializer_class = PetDatePartialUpdateModelSerializer

            return serializer_class
