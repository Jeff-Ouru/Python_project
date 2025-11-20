from django.shortcuts import render, get_object_or_404
from .models import Product

# List all products
def Products(request):
    products = Product.objects.all()
    return render(request, 'products/products_list.html', {'products': products})

# Show single product
def Products_show(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})
