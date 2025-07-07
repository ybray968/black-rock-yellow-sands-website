from django.shortcuts import render
from products.models import Product, Category

def home(request):
    """Homepage view"""
    featured_products = Product.objects.filter(featured=True, in_stock=True)[:6]
    categories = Category.objects.all()[:4]
    
    context = {
        'featured_products': featured_products,
        'categories': categories,
    }
    return render(request, 'main/home.html', context)

def about(request):
    """About page view"""
    return render(request, 'main/about.html')

def contact(request):
    """Contact page view"""
    return render(request, 'main/contact.html')
