from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Product, Category

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Product.objects.filter(in_stock=True)
        
        # Search functionality
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | 
                Q(description__icontains=search_query) |
                Q(wood_species__icontains=search_query)
            )
        
        # Filter by category
        category_slug = self.request.GET.get('category', '')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        
        # Filter by wood type
        wood_type = self.request.GET.get('wood_type', '')
        if wood_type:
            queryset = queryset.filter(wood_type=wood_type)
        
        # Filter by wood species
        wood_species = self.request.GET.get('wood_species', '')
        if wood_species:
            queryset = queryset.filter(wood_species=wood_species)
        
        # Sort options
        sort_by = self.request.GET.get('sort', 'custom')
        if sort_by == 'price_low':
            queryset = queryset.order_by('price')
        elif sort_by == 'price_high':
            queryset = queryset.order_by('-price')
        elif sort_by == 'newest':
            queryset = queryset.order_by('-created_at')
        elif sort_by == 'name':
            queryset = queryset.order_by('name')
        else:  # Default custom ordering
            # Custom ordering: Plywood Deck first, then Exterior, Interior, Parquet, Antislip MT, others
            from django.db.models import Case, When, IntegerField, Value
            queryset = queryset.annotate(
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
            ).order_by('custom_order', 'name')
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['wood_types'] = Product.WOOD_TYPES
        context['wood_species'] = Product.WOOD_SPECIES
        context['current_category'] = self.request.GET.get('category', '')
        context['current_wood_type'] = self.request.GET.get('wood_type', '')
        context['current_wood_species'] = self.request.GET.get('wood_species', '')
        context['search_query'] = self.request.GET.get('search', '')
        context['sort_by'] = self.request.GET.get('sort', 'name')
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get related products from the same category
        context['related_products'] = Product.objects.filter(
            category=self.object.category,
            in_stock=True
        ).exclude(id=self.object.id)[:4]
        return context

class CategoryProductListView(ListView):
    model = Product
    template_name = 'products/category_products.html'
    context_object_name = 'products'
    paginate_by = 12
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(category=self.category, in_stock=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

def featured_products(request):
    """View for featured products on homepage"""
    featured_products = Product.objects.filter(featured=True, in_stock=True)[:6]
    return render(request, 'products/featured_products.html', {
        'featured_products': featured_products
    })

def durability_testing(request):
    """View for durability testing page showing plywood grades and Taber test results"""
    return render(request, 'products/durability_testing.html')
