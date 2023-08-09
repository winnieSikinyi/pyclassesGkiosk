
# Create your views here.
from django.shortcuts import render ,redirect
from .forms import CartUploadForm
from .models import Cart

def cart_upload_view(request):
    form = CartUploadForm()
    return render(request,"cart/cart_upload.html", {"form":form})

def cart_list_view(request):
    carts = Cart.objects.all()
    return render(request,"cart/cart_list.html",{"carts":carts})


def cart_detail(request,id):
    cart = Cart.objects.get(id=id)
    return render(request,"cart/cart_details.html", {"cart":cart})

def cart_update_view(request, id):
    cart = Cart.objects.get(id=id)
    if request.method == 'POST':
        form = CartUploadForm(request.POST, instance=cart)
        if form.is_valid():
            form.save()
            return redirect("cart_detail_view", id=cart.id)

    else:
        form =CartUploadForm(instance=cart)
        return render(request, "cart/edit_cart.html", {'form': form})