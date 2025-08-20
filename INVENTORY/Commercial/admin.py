from django.contrib import admin
from .models import Supplier

# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('full_name','phone',)
    ordering = ('full_name',)
    search_fields = ('full_name','num_rc',)