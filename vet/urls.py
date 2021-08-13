from django.urls import path
from rest_framework.authtoken import views as authtoken_views

#Views
from .views import (
    # Pet Owners
    PetOwnersRetrieveUpdateDestroyAPIView, 
    PetOwnersListCreateAPIView, 
    PetOwnersDatesListCreateAPIView,
    # Pets
    PetListCreateAPIView,
    PetRetrieveUpdateDestroyAPIView,
    # Pet Appointments
    PetDateListCreateAPIView,
    PetDateRetrieveUpdateDestroyAPIView
    )

urlpatterns = [
    # Login
    # path("token-auth/", authtoken_views.obtain_auth_token, name="token_"),
    # Pet owners
    path("owners/", PetOwnersListCreateAPIView.as_view(), name="owners_list_apiview"),
    path("owners/<int:pk>/", PetOwnersRetrieveUpdateDestroyAPIView.as_view(), name="owners_retrieve_apiview"),
    path("owners/<int:pk>/dates/", PetOwnersDatesListCreateAPIView.as_view(), name="owners_date_list"),
    # Pets
    path("pets/", PetListCreateAPIView.as_view(), name="pet_list_apiview"),
    path("pets/<int:pk>/", PetRetrieveUpdateDestroyAPIView.as_view(), name="pet_retrieve_apiview"),
    # Appointments
    path("dates/", PetDateListCreateAPIView.as_view(), name="pet_date_list_apiview"),
    path("dates/<int:pk>/", PetDateRetrieveUpdateDestroyAPIView.as_view(), name="pet_date_retrieve_apiview")
]

# path("owners/create/", PetOwnersCreateAPIView.as_view(), name="owners_list_create_apiview"),

