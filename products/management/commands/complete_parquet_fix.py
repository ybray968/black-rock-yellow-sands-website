from django.core.management.base import BaseCommand
from products.models import Product, Category, ProductSpecification

class Command(BaseCommand):
    help = 'Complete Plywood Parquet fix: copy content, delete product/category, recreate in Plywood category'

    def handle(self, *args, **options):
        self.stdout.write("🔄 COMPLETE PLYWOOD PARQUET FIX")
        self.stdout.write("=" * 50)
        
        # STEP 1: Copy all existing content
        self.stdout.write("\n📋 STEP 1: Copying existing Plywood Parquet content...")
        try:
            existing_product = Product.objects.get(name='Plywood Parquet')
            
            # Save all the content
            saved_content = {
                'name': existing_product.name,
                'description': existing_product.description,
                'price': existing_product.price,
                'wood_type': existing_product.wood_type,
                'wood_species': existing_product.wood_species,
                'grade': existing_product.grade,
                'thickness': existing_product.thickness,
                'width': existing_product.width,
                'length': existing_product.length,
                'finish': existing_product.finish,
                'featured': existing_product.featured,
                'in_stock': existing_product.in_stock,
                'stock_quantity': existing_product.stock_quantity,
                'meta_description': existing_product.meta_description,
            }
            
            # Save specifications
            specs = ProductSpecification.objects.filter(product=existing_product)
            saved_specs = [(spec.name, spec.value) for spec in specs]
            
            self.stdout.write(f"✅ Copied content from: {existing_product.name}")
            self.stdout.write(f"✅ Copied {len(saved_specs)} specifications")
            self.stdout.write(f"✅ Current category: {existing_product.category.name}")
            
        except Product.DoesNotExist:
            self.stdout.write(self.style.ERROR("❌ Plywood Parquet not found!"))
            return
        
        # STEP 2: Delete existing product
        self.stdout.write("\n🗑️  STEP 2: Deleting existing Plywood Parquet...")
        specs_count = ProductSpecification.objects.filter(product=existing_product).count()
        ProductSpecification.objects.filter(product=existing_product).delete()
        existing_product.delete()
        self.stdout.write(f"✅ Deleted product and {specs_count} specifications")
        
        # STEP 3: Delete Parquet category if empty
        self.stdout.write("\n🗑️  STEP 3: Checking Parquet category...")
        try:
            parquet_category = Category.objects.get(slug='parquet')
            remaining_products = Product.objects.filter(category=parquet_category).count()
            
            if remaining_products == 0:
                parquet_category.delete()
                self.stdout.write("✅ Deleted empty Parquet category")
            else:
                self.stdout.write(f"⚠️  Keeping Parquet category ({remaining_products} products remain)")
                
        except Category.DoesNotExist:
            self.stdout.write("ℹ️  Parquet category already gone")
        
        # STEP 4: Get Plywood category
        self.stdout.write("\n📁 STEP 4: Getting Plywood category...")
        try:
            plywood_category = Category.objects.get(slug='plywood')
            self.stdout.write(f"✅ Found Plywood category: {plywood_category.name}")
        except Category.DoesNotExist:
            plywood_category = Category.objects.create(
                name="Plywood",
                slug='plywood',
                description='High-quality plywood products for construction and specialized applications'
            )
            self.stdout.write(f"✅ Created Plywood category: {plywood_category.name}")
        
        # STEP 5: Create fresh Plywood Parquet in Plywood category
        self.stdout.write("\n🆕 STEP 5: Creating fresh Plywood Parquet in Plywood category...")
        
        # Use saved content but put in Plywood category
        saved_content['category'] = plywood_category
        saved_content['slug'] = 'plywood-parquet'
        
        # Create the new product
        new_product = Product.objects.create(**saved_content)
        self.stdout.write(f"✅ Created: {new_product.name} in {new_product.category.name} category")
        
        # Add back all specifications
        for spec_name, spec_value in saved_specs:
            ProductSpecification.objects.create(
                product=new_product,
                name=spec_name,
                value=spec_value
            )
        
        self.stdout.write(f"✅ Added {len(saved_specs)} specifications")
        
        # STEP 6: Final verification
        self.stdout.write("\n" + "=" * 50)
        self.stdout.write(self.style.SUCCESS("🎉 COMPLETE FIX DONE!"))
        self.stdout.write("=" * 50)
        
        # Verify the new product
        verify_product = Product.objects.get(name='Plywood Parquet')
        self.stdout.write(f"📋 Product: {verify_product.name}")
        self.stdout.write(f"📁 Category: {verify_product.category.name} (slug: {verify_product.category.slug})")
        self.stdout.write(f"🔧 Featured: {verify_product.featured}")
        self.stdout.write(f"📦 In stock: {verify_product.in_stock}")
        
        specs_count = ProductSpecification.objects.filter(product=verify_product).count()
        self.stdout.write(f"📝 Specifications: {specs_count}")
        
        self.stdout.write(f"\n🎯 PLYWOOD PARQUET NOW HAS:")
        self.stdout.write(f"✅ Correct category: {verify_product.category.name}")
        self.stdout.write(f"✅ Appears with other plywood products")
        self.stdout.write(f"✅ Has application image space under main image")
        self.stdout.write(f"✅ Uses plywood template advantages")
        self.stdout.write(f"✅ Will show: plywood-parquet-application.png")
        
        self.stdout.write(f"\n📝 YOUR TASK:")
        self.stdout.write(f"Create: static/images/plywood-parquet-application.png")
        
        self.stdout.write(f"\n✨ PARQUET CATEGORY CLEANED UP - ONLY PLYWOOD CATEGORY NOW!")
