from django.urls import path
from .views import cart_upload_view
from .views import cart_list_view
from .views import cart_detail
from .views import cart_update_view


urlpatterns =[
    
    path ("carts/upload/", cart_upload_view, name = "cart_upload_view"),
    path("carts/list", cart_list_view,name ="cart_list_view"),
    path("carts/<int:id>/",cart_detail, name="cart_detail_view"),
    path("carts/edit/<int:id>", cart_update_view, name = "cart_update_view"),

    
]