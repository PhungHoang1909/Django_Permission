from django.contrib import admin
from django.http import HttpRequest
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
    
    def has_permission(self, request, obj, action):
        opts = self.opts

    
    def has_view_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False