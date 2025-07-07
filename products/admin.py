from django.contrib import admin
from .models import Category, Product, ProductImage, ProductSpecification

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'wood_type', 'wood_species', 'in_stock', 'featured']
    list_filter = ['category', 'wood_type', 'wood_species', 'in_stock', 'featured', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ProductSpecificationInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'category', 'description', 'price')
        }),
        ('Wood Specifications', {
            'fields': ('wood_type', 'wood_species', 'thickness', 'width', 'length', 'grade', 'finish')
        }),
        ('Inventory', {
            'fields': ('in_stock', 'stock_quantity')
        }),
        ('SEO & Marketing', {
            'fields': ('meta_description', 'featured')
        }),
    )

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'alt_text', 'is_primary']
    list_filter = ['is_primary']

@admin.register(ProductSpecification)
class ProductSpecificationAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'value']
    list_filter = ['name']
