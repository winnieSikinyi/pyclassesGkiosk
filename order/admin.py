from django.contrib import admin

from.models import Orders
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name","description")

admin.site.register(Orders,OrderAdmin)