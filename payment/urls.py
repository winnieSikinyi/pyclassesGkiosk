from django.urls import path
from .views import payment_upload_view
from .views import payments_list_view
from .views import payment_detail
from .views import payment_update_view

urlpatterns =[

    path ("payments/upload/", payment_upload_view, name ="payment_upload_view"),
    path("payments/list",payments_list_view,name ="payments_list_view"),
    path("payments/<int:id>/",payment_detail, name="payment_detail"),
    path("payments/edit/<int:id>",payment_update_view, name ="payment_update_view"),

]