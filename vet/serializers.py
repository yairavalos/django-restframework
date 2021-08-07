from django.db.models.fields import EmailField
from django.template.response import ContentNotRenderedError
from rest_framework import serializers
from .models import PetOwner, Pet, PetDate


# Changing Class definition by ModelSerializer
class PetOwnersListModelSerializer(serializers.ModelSerializer): 
    class Meta:
        model = PetOwner
        fields = ["id","first_name","last_name"]

class PetOwnerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ["id","first_name","last_name","address","email","phone"]


class PetListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id","name"]

class PetModelSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Pet
        fields = ["id","name","type","owner_id"]

class PetDateListModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PetDate
        fields = ["id","datetime","pet"] #Type is gone
        depth = 2

class PetDateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = ["id","datetime","type","pet"]
        #depth = 1 # This parameter its very useful I´ve tried from 1 to 2
        #lookup_field = "pk"

class PetDatePetRetrieveModelSerializer(serializers.ModelSerializer):

    pet = PetModelSerializer() # Esta la clave de OOP, sobreescribe el comportamiento por default con la definición de una clase
                                # Si la clase esta estructurada con "n" campos, entonces eso se pasa a fields implicitamente

    class Meta:
        model = PetDate
        fields = ["id", "datetime", "type", "pet"] # Si yo no sobrescribo pet en las lineas de arriba, 
                                                    # hace el comportamiento por default


class PetDatePartialUpdateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = ["datetime", "type"]


# Just Testing, doesn´t belong here
# --------------------------------------------------------------

class mySerializerTest(serializers.Serializer):
    email = serializers.EmailField()
    Content = serializers.CharField()

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get() # due that its a dictionary you can use python dict methods such as get() or pop() etc.
        return super().update(instance, validated_data)
    