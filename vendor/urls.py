from django.urls import path
from .views import category_upload_view
from .views import category_list_view
from .views import category_detail
from .views import category_update_view


urlpatterns =[
    
    path ("categories /upload/", category_upload_view, name = "category_upload_view"),
    path("categories /list", category_list_view,name ="category_list_view"),
    path("categories /<int:id>/",category_detail, name="category_detail_view"),
    path("categories /edit/<int:id>", category_update_view, name = "category_update_view"),

]