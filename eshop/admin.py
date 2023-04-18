from django.contrib import admin
from .models import Product, Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ['User', 'Name', 'Specs', 'Brand', 'Price']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Specs', 'Brand', 'Price']

admin.site.register(Cart, CartAdmin)
admin.site.register(Product, ProductAdmin)