from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .models import Product, Order
from .forms import ProductForm, OrderForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'cafe/product_list.html', {'products': products})

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order placed successfully!')
            return redirect('product_list')
    else:
        form = OrderForm()
    return render(request, 'cafe/place_order.html', {'form': form})

# Create a new product
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully!')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'cafe/product_form.html', {'form': form})

# Update existing product
def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'cafe/product_form.html', {'form': form})

# Delete a product
def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('product_list')
    return render(request, 'cafe/product_confirm_delete.html', {'product': product})
