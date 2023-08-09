from django.shortcuts import render ,redirect
from .forms import ReviewUploadForm
from .models import Review

def review_upload_view(request):
    form = ReviewUploadForm()
    return render(request,"review/review_upload.html", {"form":form})

def reviews_list_view(request):
    reviews = Review.objects.all()
    return render(request,"review/reviews_list.html",{"reviews": reviews})


def review_detail(request,id):
    review = Review.objects.get(id=id)
    return render(request,"review/review_detail.html", {"review":review})

def review_update_view(request, id):
    review = Review.objects.get(id=id)
    if request.method == 'POST':
        form = ReviewUploadForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("review_detail_view", id=review.id)

    else:
        form =ReviewUploadForm(instance=review)
        return render(request, "review/edit_review.html", {'form': form})




