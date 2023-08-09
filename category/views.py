
# Create your views here.
from django.shortcuts import render ,redirect
from .forms import CategoryUploadForm
from .models import Categories

def category_upload_view(request):
    form = CategoryUploadForm()
    return render(request,"category/category_upload.html", {"form":form})

def category_list_view(request):
    categories = Categories.objects.all()
    return render(request,"categories/category_list.html",{"categories":categories})


def category_detail(request,id):
    category = Categories.objects.get(id=id)
    return render(request,"category/category_details.html", {"category":category})

def category_update_view(request, id):
    category = Categories.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryUploadForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("category_detail_view", id=category.id)

    else:
        form =CategoryUploadForm(instance=category)
        return render(request, "category/edit_category.html", {'form': form})