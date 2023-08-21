
from django.urls import path
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import add_to_cart, cart_list, update_cart, remove_item, empty_cart

urlpatterns = [
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('product_cart/', cart_list, name='cart_list'),
    path('update_cart/<int:id>/',update_cart, name='update_cart'),
    path("remove_item/<int:id>/", remove_item, name = "remove_item"),
    path("empty/", empty_cart, name="empty_cart"),
]