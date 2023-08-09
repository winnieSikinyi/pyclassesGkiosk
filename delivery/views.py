
# Create your views here.
from django.shortcuts import render ,redirect
from .forms import DeliveryUploadForm
from .models import Delivery

def delivery_upload_view(request):
    form = DeliveryUploadForm()
    return render(request,"customer/customer_upload.html", {"form":form})

def delivery_list_view(request):
    deliverys = Delivery.objects.all()
    return render(request,"delivery/delivery_list.html",{"deliverys":deliverys})


def delivery_detail(request,id):
    delivery = Delivery.objects.get(id=id)
    return render(request,"delivery/delivery_details.html", {"delivery":delivery})

def delivery_update_view(request, id):
    delivery = Delivery.objects.get(id=id)
    if request.method == 'POST':
        form = DeliveryUploadForm(request.POST, instance=delivery)
        if form.is_valid():
            form.save()
            return redirect("delivery_detail_view", id=delivery.id)

    else:
        form =DeliveryUploadForm(instance=delivery)
        return render(request, "delivery/edit_delivery.html", {'form': form})