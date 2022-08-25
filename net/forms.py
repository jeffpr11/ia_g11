from django import forms
from .models import ImgPredict

class imgForm(forms.Form):    
    img_to_p = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))