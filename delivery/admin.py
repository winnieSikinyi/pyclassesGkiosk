from django.contrib import admin

# Register your models here.
from .models import Delivery 

class Delivery_Admin(admin.ModelAdmin):
    list_display = ('name','customer_id', 'price', 'address', 'deliver_status')

admin.site.register(Delivery, Delivery_Admin)