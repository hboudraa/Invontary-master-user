from django.contrib import admin
from .models import Supplier

# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name',)
    ordering = ('first_name',)
    search_fields = ('first_name','last_name',)