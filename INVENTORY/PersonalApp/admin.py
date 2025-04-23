from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Charger)
admin.site.register(Delegue)
admin.site.register(SG)
admin.site.register(Requisition)

@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    list_display = ('num_commune','name_commune',)
    ordering = ('num_commune',)
    search_fields = ('num_commune','name_commune',)
