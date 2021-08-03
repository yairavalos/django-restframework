from rest_framework import serializers
from .models import PetOwner, Pet


# Changing Class definition by ModelSerializer
class PetOwnersListModelSerializer(serializers.ModelSerializer): 
    class Meta:
        model = PetOwner
        fields = ["id","first_name","last_name"]

class PetOwnerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ["id","first_name","last_name","address","email","phone"]

class PetOwnerSerializer(serializers.Serializer):
    
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    address = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()

    def create(self, validated_data):
        return PetOwner.objects.create(**validated_data)


class PetOwnerUpdateSerializer(serializers.Serializer):
    
    first_name = serializers.CharField(max_length=255, required=False)
    last_name = serializers.CharField(max_length=255, required=False)
    address = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)

    def update(self, instance, validated_data):
        
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.address = validated_data.get("address", instance.address)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.save()

        return instance



# class PetListSerializer(serializers.Serializer):
#     
#     id = serializers.ReadOnlyField() #Se deja este campo como de solo lectura solo para visualización
#     name = serializers.CharField()
#     type = serializers.CharField()
#     owner_id = serializers.IntegerField() #PetOwnerSerializer #Before was PetOwnerDetails
# 
#     def create(self, validated_data):
#         return Pet.objects.create(**validated_data)


class PetListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id","name"]

class PetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id","name","type","owner_id"]

class PetUpdateSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=255)
    type = serializers.CharField()
    owner_id = serializers.IntegerField() #PetOwnerSerializer #Before was PetOwnerDetails

    def update(self, instance, validated_data):

        instance.name = validated_data.get("name", instance.name)
        instance.type = validated_data.get("type", instance.type)
        instance.owner = validated_data.get("owner", instance.owner)
        instance.save()

        return instance

