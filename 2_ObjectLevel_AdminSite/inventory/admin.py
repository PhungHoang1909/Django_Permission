from django.contrib import admin
from .models import Product
from guardian.admin import GuardedModelAdmin

@admin.register(Product)
class ProductAdmin(GuardedModelAdmin):
    list_display = ('name',)

    def has_module_permission(self, request):
        if super().has_module_permission(request):
            return True 
        
    def get_queryset(self, request):
        return super().get_queryset(request)