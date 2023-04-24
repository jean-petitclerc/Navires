from django.contrib import admin
from .models import Navire, Personne, Proprietaire, Armateur, Traversee

# Register your models here.
admin.site.register(Navire)
admin.site.register(Personne)
admin.site.register(Proprietaire)
admin.site.register(Armateur)
admin.site.register(Traversee)
