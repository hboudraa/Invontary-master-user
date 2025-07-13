from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Utilisateur)
<<<<<<< HEAD
# admin.site.register(Charger)
admin.site.register(Delegue)
admin.site.register(SG)
# admin.site.register(Requisition)
=======
admin.site.register(Charger)
admin.site.register(Delegue)
admin.site.register(SG)
admin.site.register(Requisition)
>>>>>>> f05775cd3bb9ba89bdaf8b01270083efc7d1f628

@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    list_display = ('num_commune','name_commune',)
    ordering = ('num_commune',)
    search_fields = ('num_commune','name_commune',)
<<<<<<< HEAD

@admin.register(Charger)
class ChargerAdmin(admin.ModelAdmin):
    list_display = ('commune','name_french','phone')
    ordering = ('commune',)
    search_fields = ('commune','name_french')

@admin.register(Requisition)
class RequisitionAdmin(admin.ModelAdmin):
    list_display = ('commune','name_french','phone')
    ordering = ('commune',)
    search_fields = ('commune','name_french')
=======
>>>>>>> f05775cd3bb9ba89bdaf8b01270083efc7d1f628
