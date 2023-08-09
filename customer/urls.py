from django.urls import path
from .views import customer_upload_view
from .views import customer_list_view
from .views import customer_detail
from .views import customer_update_view


urlpatterns =[
    
    path ("customers/upload/", customer_upload_view, name = "customer_uploadview"),
    path("customers/list",customer_list_view,name ="customer_list_view"),
    path("customers/<int:id>/",customer_detail, name="customer_detail_view"),
    path("customers/edit/<int:id>", customer_update_view, name = "customer_update_view"),

    
]