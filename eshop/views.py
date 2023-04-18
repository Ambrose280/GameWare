from django.shortcuts import render, redirect
from . models import*
from eshop.models import Product
# Create your views here.
from django.contrib.auth.models import User
def products(request):
    products = Product.objects.all()
    cart = Cart.objects.all()
    total = len(cart) 
    # print(f"total----->{total}")
    if products:
        context = {"products":products, "total":total}
        return render(request, 'products.html', context)
    return render(request, "products.html", context=
    {"msg":"no available product", "total":total})


def addToCart(request, pk):
    products = Product.objects.filter(pk = pk).values()
    # print(f"product----->{products}")
    "[{'id': 1, 'name': 'bicycle', 'price': Decimal('3000.00'), 'description': 'riding bicycle for journeys', 'image': 'Bicycle.jpg'}]"
    user = request.user
    user_data = User.objects.filter(username = user ).values()
    userID = user_data[0]["id"]
    data = products[0]
    name = data["name"]
    price = data["price"]
    description = data["description"]
    image = data["image"]
    cart_data = Cart.objects.create(user_id = userID, name = name, price = price, description = description, image=image)
    cart_data.save()
    return redirect("products")


def cartPage(request):
    cart = Cart.objects.all()
    cartitems = Cart.objects.all().values()
    total = len(cart) 
    user = request.user
    print(f"cart--->{cart}")
    print(f"cart--->{user}")
    "[{'id': 1, 'user_id': 3, 'name': 'bicycle', 'price': Decimal('3000.00'), 'description': 'riding bicycle for journeys', 'image': 'Bicycle.jpg'}, {'id': 2, 'user_id': 3, 'name': 'xbox', 'price': Decimal('4000000.00'), 'description': 'gamin experience', 'image': 'Xbox_console.jpg'}, {'id': 3, 'user_id': 3, 'name': 'xbox', 'price': Decimal('4000000.00'), 'description': 'gamin experience', 'image': 'Xbox_console.jpg'}, {'id': 4, 'user_id': 3, 'name': 'oven', 'price': Decimal('2000.00'), 'description': 'cooking oven', 'image': 'Oven.jpg'}]"
    l = []
    for x in cartitems:
        price = x["Price"]
        l.append(price)
    total_price = sum(l)
    if cart:
        context = {"cart":cart, "total":total, "total_price":total_price}
        return render(request, 'cart.html', context)
    return render(request, "cart.html", context=
    {"msg":"cart is empty please add product", "total":total})


def deleteProduct(request, pk):
    cart = Cart.objects.filter(pk = pk)
    cart.delete()
    return redirect("cart")
    