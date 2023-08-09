
# Create your views here.
from django.shortcuts import render ,redirect
from .forms import VendorUploadForm
from .models import vendor

def vendor_upload_view(request):
    form = VendorUploadForm()
    return render(request,"vendor/vendor_upload.html", {"form":form})

def vendor_list_view(request):
    vendors = Categories.objects.all()
    return render(request,"vendor/vendor_list.html",{"vendors":vendors})


def category_detail(request,id):
    category = Category.objects.get(id=id)
    return render(request,"category/category_details.html", {"category":category})

def category_update_view(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryUploadForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("category_detail_view", id=category.id)

    else:
        form =CategoryUploadForm(instance=category)
        return render(request, "category/edit_category.html", {'form': form})