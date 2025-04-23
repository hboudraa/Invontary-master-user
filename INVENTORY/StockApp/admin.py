from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(FicheStockEntr)
admin.site.register(FicheStockSortie)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'total')
    ordering = ('name',)
    search_fields = ('name', )

@admin.register(DemandClass)
class DemandClassAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'name_demand', 'quantity',)
    
