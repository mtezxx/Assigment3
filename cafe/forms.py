from django import forms
from .models import Order
from .models import Product

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity']

class ProductForm(forms.ModelForm):
     class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'price']
        
     
