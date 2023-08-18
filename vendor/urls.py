from django.urls import path
from .views import vendor_upload_view
from .views import vendor_list_view
from .views import vendor_detail
from .views import vendor_update_view


urlpatterns =[
    
    path ("vendor/upload/", vendor_upload_view, name = "vendor_upload_view"),
    path("vendor/list",vendor_list_view,name ="vendor_list_view"),
    path("vendor/<int:id>/",vendor_detail, name="vendor_detail_view"),
    path("vendor/edit/<int:id>",vendor_update_view, name ="vendor_update_view"),

]