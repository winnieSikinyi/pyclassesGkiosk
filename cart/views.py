from django.shortcuts import render, redirect
from .models import Cart
# from .forms import ProductCartGetForm
from datetime import datetime
from .models import Product

def cart_list(request):
    product_cart = Cart.objects.all()
    
    total_cart_price = 0

    for item in product_cart:
        item.total_price = item.product_price * item.product_quantity
        total_cart_price += item.total_price

    return render(request, "cart/cart_list.html", {"product_cart": product_cart, "total_cart_price": total_cart_price})


def update_cart(request, id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item = Cart.objects.get(id=id)
        if quantity > 0:
            cart_item.product_quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart_list')



def remove_item(request, id):
    cart_item = Cart.objects.get(id=id)
    cart_item.delete()

    return redirect('cart_list')
def empty_cart(request):
    Cart.objects.all().delete()
    return redirect("cart_list")

def add_to_cart(request, id):
    product = Product.objects.get(id=id)

    cart_item = Cart (
        product_name = product.name,
        product_price = product.price,
        product_image = product.image,
        product_quantity = 1,
        date_added=datetime.now(),
    )
    cart_item.save()

    return redirect("products_list")