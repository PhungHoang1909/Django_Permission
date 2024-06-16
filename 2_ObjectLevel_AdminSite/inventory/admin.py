from django.contrib import admin
from .models import Product
from guardian.admin import GuardedModelAdmin

@admin.register(Product)
class ProductAdmin(GuardedModelAdmin):
    list_display = ('name',)
    