from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q  # is used to generate a search query
from .models import Product

# Create your views here.


def all_products(request):
    """Shows all products, inclusive of sorting and search queries"""

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.query(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)  # i is for case insensitive
            products = products.filter(queries)

    context = {
        'products': products,
        'search_item': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """Shows detailed information of a chosen product item"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)