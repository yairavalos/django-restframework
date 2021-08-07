from django.contrib import admin
from .models import Pet, PetDate, PetOwner

# Register your models here.

admin.site.register(Pet)
admin.site.register(PetOwner)
admin.site.register(PetDate)