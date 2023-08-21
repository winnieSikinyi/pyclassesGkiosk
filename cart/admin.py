from django.contrib import admin
# Register your models here.
from .models import Cart
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display=("product_name", "product_price", "product_quantity", "product_image","date_added")
admin.site.register(Cart,CartAdmin)
