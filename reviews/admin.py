from django.contrib import admin

from  .models import Reviews

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["review_name"]

admin.site.register(Reviews,ReviewAdmin)
