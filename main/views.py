from django.shortcuts import render
from products.models import Product, Category

def home(request):
    """Homepage view"""
    # Use same custom ordering as products page
    from django.db.models import Case, When, IntegerField, Value
    
    featured_products = Product.objects.filter(featured=True, in_stock=True).annotate(
        custom_order=Case(
            When(name__icontains='Deck', then=Value(1)),
            When(name__icontains='Exterior Birch', then=Value(2)),
            When(name__icontains='Birch Exterior', then=Value(2)),
            When(name__icontains='Interior Birch', then=Value(3)),
            When(name__icontains='Birch Interior', then=Value(3)),
            When(name__icontains='Parquet', then=Value(4)),
            When(name__icontains='Antislip MT', then=Value(5)),
            When(name__icontains='Antislip Wire', then=Value(5)),
            default=Value(6),
            output_field=IntegerField()
        )
    ).order_by('custom_order', 'name')[:6]
    
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
