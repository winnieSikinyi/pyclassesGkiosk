from django.urls import path
from .views import category_upload_view
from .views import category_list_view
from .views import category_detail
from .views import category_update_view


urlpatterns =[
    
    path("category/upload/", category_upload_view, name = "category_upload_view"),
    path("category/list", category_list_view,name ="category_list_view"),
    path("category/<int:id>/",category_detail, name="category_detail_view"),
    path("category/edit/<int:id>", category_update_view, name = "category_update_view"),

]