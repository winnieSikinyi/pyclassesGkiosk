from django.urls import path
from .views import order_upload_view
from .views import order_list_view
from .views import order_detail
from .views import order_update_view


urlpatterns =[
    path ("orders/upload/", order_upload_view, name = "order_uploadview"),
    path("orders/list",order_list_view,name ="order_list_view"),
    path("orders/<int:id>/",order_detail, name="order_detail_view"),

    path("orders/edit/<int:id>", order_update_view, name = "order_update_view"),

    
]