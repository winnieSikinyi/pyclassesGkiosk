from django.urls import path
from .views import signup_upload_view
from .views import signup_list_view
from .views import signup_detail
from .views import signup_update_view

urlpatterns =[

    path("signup/upload/", signup_upload_view, name ="signup_upload_view"),
    path("signup/list",signup_list_view,name ="signup_list_view"),
    path("signup/<int:id>/",signup_detail, name="signup_detail"),
    path("signup/edit/<int:id>",signup_update_view, name ="signup_update_view"),

]