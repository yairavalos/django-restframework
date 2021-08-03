from django.shortcuts import get_object_or_404, render
from django.views import generic

# Create your views here.
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

# Models
from .models import PetOwner,Pet
from .serializers import PetOwnerListSerializer, PetOwnerSerializer, PetOwnerUpdateSerializer, PetListSerializer, PetUpdateSerializer

# Serializers
# from .serializers import PetOwnerListSerializer

class PetOwnersListCreateAPIView(APIView):
    """
    View to list all pet owners in the system
    """
    serializer_class = PetOwnerListSerializer

    #sobre-escribo el método http que quiero manejar
    #siempre 2 parametros, self y request
    def get(self, request):
        
        owners_queryset = PetOwner.objects.all()
        serializer = self.serializer_class(owners_queryset, many=True)

        return Response(data=serializer.data)

    def post(self, request):

        print(request.data)
        serializer = PetOwnerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        created_instance = serializer.save()

        print(created_instance.__dict__)
        return Response({})


class PetOwnerRetrieveUpdateDestroyAPIView(APIView):
    """
    View to retrieve a Pet Owner by Id
    """

    serializer_class = PetOwnerSerializer

    def get(self, request, pk): # La otra opción es extraer pk desde request, pero necesitamos imprimirlo en consola para descubrirlo

        print("This is request result:")
        print(pk)

        owner = get_object_or_404(PetOwner, id=pk)
        serializer = self.serializer_class(owner)

        return Response(serializer.data) #data=serializer.data

    def patch(self, request, pk): # Se usa pk por convencion, declarado así desde urls.py

        owner = get_object_or_404(PetOwner, id=pk)
        serializer = PetOwnerUpdateSerializer(instance=owner, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_instance = serializer.save()
        serialized_instance = self.serializer_class(updated_instance)

        return Response(serialized_instance.data)

    def delete(self, request, pk):

        owner = get_object_or_404(PetOwner, id=pk)
        owner.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class PetListAPIView(APIView):
    """
    View to list all pets
    """
    serializer_class = PetListSerializer

    def get(self, request):

        pets_queryset = Pet.objects.all()
        serializer = self.serializer_class(pets_queryset, many=True)

        return Response(data=serializer.data)

    def post(self, request):

        print(request.data)
        serializer = PetListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        created_instance = serializer.save()

        print(created_instance.__dict__)
        return Response({})
    
class PetRetrieveUpdateDestroyAPIView(APIView):
    """
    View to Update Pet Details
    """

    serializer_class = PetUpdateSerializer

    def get(self, request, pk):

        pet = get_object_or_404(Pet, id=pk)
        serializer = self.serializer_class(pet)

        return Response(serializer.data)

    def patch(self, request, pk):

        pet = get_object_or_404(Pet, id=pk)
        serializer = PetUpdateSerializer(instance=pet, data=request.data)
        serializer.is_valid(raise_exception=True)
        update_instance = serializer.save()
        serialized_instance = self.serializer_class(update_instance)

        return Response(serialized_instance.data)

    def delete(self, request, pk):

        pet = get_object_or_404(Pet, id=pk)
        pet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
