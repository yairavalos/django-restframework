from django.urls import path

#Views
from .views import PetOwnersListAPIView, PetOwnerRetrieveAPIView, PetListAPIView, PetRetrieveAPIView  # PetOwnersListCreateAPIView, PetOwnerRetrieveUpdateDestroyAPIView, PetListAPIView, PetRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("owners/", PetOwnersListAPIView.as_view(), name="owners_list_apiview"),
    path("owners/<int:pk>/", PetOwnerRetrieveAPIView.as_view(), name="owners_retrieve_apiview"),
    path("pets/", PetListAPIView.as_view(), name="pet_list_apiview"),
    path("pets/<int:pk>/", PetRetrieveAPIView.as_view(), name="pet_retrieve_apiview"),
]


# urlpatterns = [
#      path("owners/", PetOwnersListCreateAPIView.as_view(), name="owners_list_create"),
#      path("owners/<int:pk>/", PetOwnerRetrieveUpdateDestroyAPIView.as_view(), name="owners_retrieve_update_destroy"),
#      path("pets/", PetListAPIView.as_view(), name="pet_list"),
#      path("pets/<int:pk>/", PetRetrieveUpdateDestroyAPIView.as_view(), name="pet_retrieve_update_destroy"),
# ]

# example: path("owners/<int:pk>/")