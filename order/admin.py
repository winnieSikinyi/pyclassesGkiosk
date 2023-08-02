from django.contrib import admin

# Register your models here.
from .models import Order
class Order_Admin(admin.ModelAdmin):
    list_display=('name','customer_id','quantity','price')

admin.site.register(Order, Order_Admin)




    