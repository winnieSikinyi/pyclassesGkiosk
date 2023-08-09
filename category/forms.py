from django import forms
from .models import Categories

# from models import Category

class CategoryUploadForm(forms.ModelForm):
    class Meta: 
        model = Categories
        fields = '__all__'