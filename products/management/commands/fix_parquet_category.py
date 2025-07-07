from django.core.management.base import BaseCommand
from products.models import Product, Category

class Command(BaseCommand):
    help = 'Move Plywood Parquet from Parquet category to Plywood category'

    def handle(self, *args, **options):
        self.stdout.write("Fixing Plywood Parquet category...")
        
        try:
            # Find the Plywood Parquet product
            parquet_product = Product.objects.get(name='Plywood Parquet')
            self.stdout.write(f"Found product: {parquet_product.name}")
            self.stdout.write(f"Current category: {parquet_product.category.name}")
            
            # Get the Plywood category
            plywood_category = Category.objects.get(slug='plywood')
            self.stdout.write(f"Target category: {plywood_category.name}")
            
            # Update the product's category
            parquet_product.category = plywood_category
            parquet_product.save()
            
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully moved '{parquet_product.name}' to '{plywood_category.name}' category"
                )
            )
            
            # Verify the change
            updated_product = Product.objects.get(name='Plywood Parquet')
            self.stdout.write(f"Verification: Product is now in '{updated_product.category.name}' category")
            
        except Product.DoesNotExist:
            self.stdout.write(
                self.style.ERROR("Plywood Parquet product not found")
            )
            self.stdout.write("You may need to run the add_plywood_parquet.py script first")
            
        except Category.DoesNotExist:
            self.stdout.write(
                self.style.ERROR("Plywood category not found")
            )
            self.stdout.write("Please ensure the Plywood category exists")
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"Error: {e}")
            )
