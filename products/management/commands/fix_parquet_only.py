from django.core.management.base import BaseCommand
from products.models import Product, Category, ProductSpecification

class Command(BaseCommand):
    help = 'Fix Plywood Parquet - move it to Plywood category without touching other products'

    def handle(self, *args, **options):
        self.stdout.write("🔧 FIXING PLYWOOD PARQUET ONLY - NO OTHER PRODUCTS TOUCHED")
        self.stdout.write("=" * 60)
        
        # Step 1: Find existing Plywood Parquet
        try:
            old_product = Product.objects.get(name='Plywood Parquet')
            self.stdout.write(f"Found existing product: {old_product.name}")
            self.stdout.write(f"Current category: {old_product.category.name} (slug: {old_product.category.slug})")
            
            # Step 2: Get Plywood category
            try:
                plywood_category = Category.objects.get(slug='plywood')
                self.stdout.write(f"Target category: {plywood_category.name}")
                
                # Step 3: Simply move the product to Plywood category
                old_product.category = plywood_category
                old_product.save()
                
                self.stdout.write(
                    self.style.SUCCESS(
                        f"✅ SUCCESS: Moved '{old_product.name}' to '{plywood_category.name}' category"
                    )
                )
                
                # Step 4: Verify the change
                updated_product = Product.objects.get(name='Plywood Parquet')
                self.stdout.write(f"✅ Verified: Product is now in '{updated_product.category.name}' category")
                
                # Step 5: Show what this enables
                self.stdout.write("\n" + "=" * 60)
                self.stdout.write("🎯 WHAT PLYWOOD PARQUET NOW HAS:")
                self.stdout.write("=" * 60)
                self.stdout.write("✅ Appears with other plywood products")
                self.stdout.write("✅ Uses plywood template advantages (Parquet-specific section)")
                self.stdout.write("✅ Shows main image: plywood-parquet.png")
                self.stdout.write("✅ Has application image space under main image")
                self.stdout.write("✅ Will show: plywood-parquet-application.png")
                
                self.stdout.write("\n📝 YOUR TASK:")
                self.stdout.write("Create application image: static/images/plywood-parquet-application.png")
                
            except Category.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR("❌ ERROR: Plywood category not found!")
                )
                
        except Product.DoesNotExist:
            self.stdout.write(
                self.style.ERROR("❌ ERROR: Plywood Parquet product not found!")
            )
        except Product.MultipleObjectsReturned:
            self.stdout.write(
                self.style.ERROR("❌ ERROR: Multiple Plywood Parquet products found!")
            )
