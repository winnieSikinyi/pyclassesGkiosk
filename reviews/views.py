from django.shortcuts import render ,redirect
from .forms import ReviewUploadForm
from .models import Reviews

def review_upload_view(request):
    form = ReviewUploadForm()
    return render(request,"review/reviews_upload.html", {"form":form})

def reviews_list_view(request):
    reviews = Reviews.objects.all()
    return render(request,"reviews/reviews_list.html",{"reviews": reviews})


def review_detail(request,id):
    reviews = Reviews.objects.get(id=id)
    return render(request,"reviews/reviews_details.html", {"reviews":reviews})

def review_update_view(request, id):
    reviews = Reviews.objects.get(id=id)
    if request.method == 'POST':
        form = ReviewUploadForm(request.POST, instance=reviews)
        if form.is_valid():
            form.save()
            return redirect("reviews_details_view", id=reviews.id)

    else:
        form =ReviewUploadForm(instance=reviews)
        return render(request, "reviews/edit_reviews.html", {'form': form})




