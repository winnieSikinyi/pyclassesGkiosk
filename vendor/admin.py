from django.contrib import admin
from inventory.models import Vendor
# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")
admin.site.register(Vendor, VendorAdmin)
