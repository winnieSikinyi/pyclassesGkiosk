from django.contrib import admin

# Register your models here.
from.models import Signup
from.models import Login
# Register your models here.
class SignupAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","confirm_password","phone","email","password")
admin.site.register(Signup,SignupAdmin)
class LoginAdmin(admin.ModelAdmin):
    list_display=("user_name","email","password")
admin.site.register(Login,LoginAdmin)