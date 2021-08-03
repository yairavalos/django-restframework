from django.urls import path

#Views
from .views import PetOwnersListCreateAPIView, PetOwnerRetrieveUpdateDestroyAPIView, PetListAPIView, PetRetrieveUpdateDestroyAPIView

urlpatterns = [
     path("owners/", PetOwnersListCreateAPIView.as_view(), name="owners_list_create"),
     path("owners/<int:pk>/", PetOwnerRetrieveUpdateDestroyAPIView.as_view(), name="owners_retrieve_update_destroy"),
     path("pets/", PetListAPIView.as_view(), name="pet_list"),
     path("pets/<int:pk>/", PetRetrieveUpdateDestroyAPIView.as_view(), name="pet_retrieve_update_destroy"),
]

# example: path("owners/<int:pk>/")