from django import forms

from .models import Product

class ProductForm(forms.Modelform):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
        ]