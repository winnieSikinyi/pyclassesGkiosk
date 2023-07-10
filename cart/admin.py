from django.contrib import admin
# Register your models here.
from .models import Cart
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display=("customer_ID", "list_of_items", "quantity_of_items")
admin.site.register(Cart,CartAdmin)
