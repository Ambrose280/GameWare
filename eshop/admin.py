from django.contrib import admin
from .models import Product



class ProductAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Specs', 'Brand']

admin.site.register(Product, ProductAdmin)