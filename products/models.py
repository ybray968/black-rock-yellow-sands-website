from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:category', kwargs={'slug': self.slug})

class Product(models.Model):
    WOOD_TYPES = [
        ('hardwood', 'Hardwood'),
        ('softwood', 'Softwood'),
        ('engineered', 'Engineered Wood'),
    ]
    
    WOOD_SPECIES = [
        ('oak', 'Oak'),
        ('pine', 'Pine'),
        ('maple', 'Maple'),
        ('birch', 'Birch'),
        ('walnut', 'Walnut'),
        ('cherry', 'Cherry'),
        ('mahogany', 'Mahogany'),
        ('teak', 'Teak'),
    ]
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Product specifications
    wood_type = models.CharField(max_length=20, choices=WOOD_TYPES, blank=True)
    wood_species = models.CharField(max_length=20, choices=WOOD_SPECIES, blank=True)
    thickness = models.CharField(max_length=50, blank=True)  # e.g., "15mm", "3/4 inch"
    width = models.CharField(max_length=50, blank=True)
    length = models.CharField(max_length=50, blank=True)
    grade = models.CharField(max_length=50, blank=True)  # e.g., "A", "B", "Premium"
    finish = models.CharField(max_length=100, blank=True)  # e.g., "Natural", "Stained", "Lacquered"
    
    # Stock and availability
    in_stock = models.BooleanField(default=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    
    # SEO and metadata
    meta_description = models.CharField(max_length=160, blank=True)
    featured = models.BooleanField(default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.product.name} - Image"

class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')
    name = models.CharField(max_length=100)  # e.g., "Moisture Content", "Density"
    value = models.CharField(max_length=200)  # e.g., "8-12%", "650 kg/m³"
    
    def __str__(self):
        return f"{self.product.name} - {self.name}: {self.value}"
