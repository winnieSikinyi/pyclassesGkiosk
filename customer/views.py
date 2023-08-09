
# Create your views here.
from django.shortcuts import render ,redirect
from .forms import CustomerUploadForm
from .models import Customer

def customer_upload_view(request):
    form = CustomerUploadForm()
    return render(request,"customer/customer_upload.html", {"form":form})

def customer_list_view(request):
    customers = Customer.objects.all()
    return render(request,"customer/customers_list.html",{"customers":customers})


def customer_detail(request,id):
    customer = Customer.objects.get(id=id)
    return render(request,"customer/customer_details.html", {"customer":customer})

def customer_update_view(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        form = CustomerUploadForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_detail_view", id=customer.id)

    else:
        form =CustomerUploadForm(instance=customer)
        return render(request, "customer/edit_customer.html", {'form': form})