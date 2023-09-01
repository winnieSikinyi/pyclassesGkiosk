from django import forms
from .models import Signup

class SignupUploadForm(forms.ModelForm):
    class Meta: 
        model = Signup
        fields = "__all__"