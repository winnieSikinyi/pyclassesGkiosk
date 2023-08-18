
# Create your views here.
from django.shortcuts import render ,redirect
from .forms import VendorUploadForm
from vendor.models import Vendor

def vendor_upload_view(request):
    form = VendorUploadForm()
    return render(request,"vendor/vendor_upload.html", {"form":form})

def vendor_list_view(request):
    vendors = Vendor.objects.all()
    return render(request,"vendor/vendor_list.html",{"vendors":vendors})


def vendor_detail(request,id):
    vendor = Vendor.objects.get(id=id)
    return render(request,"vendor/vendor_details.html", {"vendor":vendor})

def vendor_update_view(request, id):
    vendor = Vendor.objects.get(id=id)
    if request.method == 'POST':
        form = VendorUploadForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect("vendor_detail_view", id=vendor.id)

    else:
        form =VendorUploadForm(instance=vendor)
        return render(request, "vendor/edit_vendor.html", {'form': form})