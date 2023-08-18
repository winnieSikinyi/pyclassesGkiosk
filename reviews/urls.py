from django.urls import path
from .views import review_upload_view
from .views import reviews_list_view
from .views import review_detail
from .views import review_update_view

urlpatterns =[
    path("reviews/upload/", review_upload_view, name="review_upload_view"),
    path("reviews/list/",reviews_list_view,name ="reviews_list_view"),
    path("reviews/<int:id>/",review_detail,name="reviews_details_view"),
    path("reviews/edit/<int:id>",review_update_view,name="reviews_update_view"),
    
]