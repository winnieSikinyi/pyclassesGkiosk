
# Create your views here.
from django.shortcuts import render ,redirect
from .forms import OrderUploadForm
from .models import Order

def order_upload_view(request):
    form = OrderUploadForm()
    return render(request,"order/order_upload.html", {"form":form})

def order_list_view(request):
    orders = Order.objects.all()
    return render(request,"order/order_list.html",{"orders":orders})


def order_detail(request,id):
    order = Order.objects.get(id=id)
    return render(request,"order/order_details.html", {"order":order})

def order_update_view(request, id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        form = OrderUploadForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("order_detail_view", id=order.id)

    else:
        form =OrderUploadForm(instance=order)
        return render(request, "order/edit_order.html", {'form': form})