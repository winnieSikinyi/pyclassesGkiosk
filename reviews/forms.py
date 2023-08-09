from django import forms
from .models import Reviews

class ReviewUploadForm(forms.ModelForm):
    class Meta: 
        model = Review
        fields = "__all__"