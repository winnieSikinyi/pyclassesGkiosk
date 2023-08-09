from django.urls import path
from .views import delivery_upload_view
from .views import delivery_list_view
from .views import delivery_detail
from .views import delivery_update_view


urlpatterns =[
    
    path ("deliverys/upload/", delivery_upload_view, name = "delivery_uploadview"),
    path("deliverys/list",delivery_list_view,name ="delivery_list_view"),
    path("deliverys/<int:id>/",delivery_detail, name="delivery_detail_view"),
    path("deliverys/edit/<int:id>", delivery_update_view, name = "delivery_update_view"),

    
]