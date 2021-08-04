from django.urls import path

#Views
from .views import PetOwnersRetrieveUpdateDestroyAPIView, PetOwnersListCreateAPIView, PetOwnerRetrieveAPIView, PetListCreateAPIView, PetRetrieveAPIView

urlpatterns = [
    path("owners/", PetOwnersListCreateAPIView.as_view(), name="owners_list_apiview"),
    path("owners/<int:pk>/", PetOwnersRetrieveUpdateDestroyAPIView.as_view(), name="owners_retrieve_apiview"),
    path("pets/", PetListCreateAPIView.as_view(), name="pet_list_apiview"),
    path("pets/<int:pk>/", PetRetrieveAPIView.as_view(), name="pet_retrieve_apiview"),
]

# path("owners/create/", PetOwnersCreateAPIView.as_view(), name="owners_list_create_apiview"),