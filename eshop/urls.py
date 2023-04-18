from django.urls import path

from . import views

urlpatterns = [
    path("", views.products, name="products"),
    path('add_products/<int:pk>', views.addToCart, name="add_products"),
    path('cart/', views.cartPage, name="cart"),
    path('delete/<int:pk>', views.deleteProduct, name="delete"),
]