from django.shortcuts import render ,redirect
from .forms import PaymentUploadForm
from .models import Payment

def payment_upload_view(request):
    form = PaymentUploadForm()
    return render(request,"payment/payment_upload.html", {"form":form})

def payments_list_view(request):
    payments = Payment.objects.all()
    return render(request,"payment/payment_list.html",{"payment": payments})


def payment_detail(request,id):
    payment = Payment.objects.get(id=id)
    return render(request,"payment/payment_detail.html", {"payment":payment})

def payment_update_view(request, id):
    payment = Payment.objects.get(id=id)
    if request.method == 'POST':
        form = PaymentUploadForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect("payment_detail_view", id=payment.id)

    else:
        form =PaymentUploadForm(instance=payment)
        return render(request, "payment/edit_payment.html", {'form': form})





