from django.shortcuts import render ,redirect
from .forms import SignupUploadForm
from .models import Signup

def signup_upload_view(request):
    form = SignupUploadForm()
    return render(request,"signup/signup_upload.html", {"form":form})

def signup_list_view(request):
    signups = Signup.objects.all()
    return render(request,"signup/signup_list.html",{"signups": signups})


def signup_detail(request,id):
    signup = Signup.objects.get(id=id)
    return render(request,"signup/signup_detail.html", {"signup":signup})

def signup_update_view(request, id):
    signup = Signup.objects.get(id=id)
    if request.method == 'POST':
        form = SignupUploadForm(request.POST, instance=signup)
        if form.is_valid():
            form.save()
            return redirect("signup_detail", id=id)

    else:
        form =SignupUploadForm(instance=signup)
        return render(request, "signup/edit_signup.html", {'form': form})





