#!/usr/bin/env python
"""
Generate QR codes for all 12 products with company logo embedded
Each QR code will link to the products page and scroll to the specific product
"""

import os
import sys
import django
import qrcode
from PIL import Image, ImageDraw, ImageFont

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product

def create_qr_with_logo(product_name, url, logo_path, output_dir):
    """Create a QR code with logo and product name"""
    
    # Create QR code with custom styling
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for logo embedding
        box_size=10,
        border=4,
    )
    
    qr.add_data(url)
    qr.make(fit=True)

    # Create QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Load and resize logo
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        
        # Calculate logo size (about 18% of QR code size for better balance)
        qr_width, qr_height = qr_img.size
        logo_size = min(qr_width, qr_height) // 6  # Slightly smaller for better scanning
        
        # Resize logo maintaining aspect ratio
        logo_aspect = logo.width / logo.height
        if logo_aspect > 1:  # Logo is wider than tall
            new_width = logo_size
            new_height = int(logo_size / logo_aspect)
        else:  # Logo is taller than wide or square
            new_width = int(logo_size * logo_aspect)
            new_height = logo_size
            
        logo = logo.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Create a white circular background for better visibility
        bg_size = max(new_width, new_height) + 16
        logo_bg = Image.new('RGBA', (bg_size, bg_size), (255, 255, 255, 255))
        
        # Center the logo on the background
        logo_pos = ((bg_size - new_width) // 2, (bg_size - new_height) // 2)
        
        # Handle transparency properly
        if logo.mode == 'RGBA':
            logo_bg.paste(logo, logo_pos, logo)
        else:
            logo_bg.paste(logo, logo_pos)
        
        # Paste logo in center of QR code
        qr_img = qr_img.convert('RGBA')
        qr_logo_pos = ((qr_width - bg_size) // 2, (qr_height - bg_size) // 2)
        qr_img.paste(logo_bg, qr_logo_pos)
    
    # Convert back to RGB for saving as PNG
    qr_img = qr_img.convert('RGB')
    
    # Create final image with product name below QR code
    final_height = qr_img.height + 100  # Extra space for text
    final_img = Image.new('RGB', (qr_img.width, final_height), (255, 255, 255))
    
    # Paste QR code
    final_img.paste(qr_img, (0, 0))
    
    # Add product name text
    draw = ImageDraw.Draw(final_img)
    
    # Try to use Inter font (website font), fallback to alternatives
    font_size = 20
    try:
        # Try to download and use Inter font (same as website)
        font = ImageFont.truetype("C:/Windows/Fonts/Inter-Medium.ttf", font_size)
    except:
        try:
            # Fallback to system fonts that look similar
            font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", font_size)
        except:
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except:
                font = ImageFont.load_default()
    
    # Calculate text position (centered)
    text_bbox = draw.textbbox((0, 0), product_name, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_x = (qr_img.width - text_width) // 2
    text_y = qr_img.height + 25
    
    # Draw text without shadow (clean like website)
    draw.text((text_x, text_y), product_name, fill=(26, 32, 44), font=font)  # Using website's text color
    
    # Save the final image
    output_path = os.path.join(output_dir, f"{product_name.replace(' ', '_').replace('(', '').replace(')', '')}_QR.png")
    final_img.save(output_path, 'PNG', quality=95)
    
    return output_path

def generate_all_qr_codes():
    """Generate QR codes for all products"""
    
    # Base URL for individual products
    base_url = "https://www.braysint.com/products/"
    
    # Logo path (using the highest quality logo)
    logo_path = "static/images/brays-logo.png"  # 419KB high-quality logo
    
    # Create output directory
    output_dir = "product_qr_codes"
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all products
    products = Product.objects.all().order_by('name')
    
    print("🎯 GENERATING QR CODES FOR ALL PRODUCTS")
    print("=" * 50)
    print(f"📍 Base URL: {base_url}")
    print(f"🏢 Logo: {logo_path}")
    print(f"📁 Output directory: {output_dir}")
    print(f"📦 Total products: {products.count()}")
    
    # Check which font will be used
    try:
        test_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 20)
        font_name = "Segoe UI (similar to Inter)"
    except:
        font_name = "System default font"
    
    print(f"🔤 Font: {font_name}")
    print(f"✨ Typography: No shadows, clean text matching website style")
    print()
    
    generated_qr_codes = []
    
    for i, product in enumerate(products, 1):
        print(f"🔄 Generating QR code {i}/12: {product.name}")
        
        # Generate anchor link to specific product on products page
        product_url = f"{base_url}#product-{product.id}"
        
        print(f"   🔗 URL: {product_url}")
        print(f"   ⚓ Anchor: #product-{product.id} (scrolls to product {product.id})")
        
        try:
            output_path = create_qr_with_logo(
                product_name=product.name,
                url=product_url,
                logo_path=logo_path,
                output_dir=output_dir
            )
            
            generated_qr_codes.append({
                'product': product.name,
                'file': output_path,
                'category': product.category.name
            })
            
            print(f"   ✅ Saved: {os.path.basename(output_path)}")
            
        except Exception as e:
            print(f"   ❌ Error generating QR for {product.name}: {str(e)}")
    
    # Summary
    print("\n" + "=" * 50)
    print("🎉 QR CODE GENERATION COMPLETED!")
    print("=" * 50)
    print(f"✅ Successfully generated: {len(generated_qr_codes)}/12 QR codes")
    print(f"📁 All files saved in: {output_dir}/")
    print()
    
    print("📋 GENERATED QR CODES:")
    print("-" * 50)
    for qr_info in generated_qr_codes:
        filename = os.path.basename(qr_info['file'])
        print(f"   📦 {qr_info['product']}")
        print(f"      📄 File: {filename}")
        print(f"      🏷️  Category: {qr_info['category']}")
        print()
    
    print("🎯 FEATURES OF GENERATED QR CODES:")
    print("   ✅ Each QR code links to products page and scrolls to specific product")
    print("   ✅ High-quality company logo embedded in center")
    print("   ✅ Product name displayed below QR code")
    print("   ✅ High-quality PNG format (print-ready)")
    print("   ✅ Professional styling with clean typography")
    print("   ✅ High error correction (logo embedding compatible)")
    print()
    
    print("📱 TESTING:")
    print("   🔗 Each QR code opens products page and auto-scrolls to specific product")
    print("   ⚓ Uses anchor links (#product-ID) for precise scrolling")
    print("   📸 Test with any QR code scanner app")
    print()
    
    print("🖨️  READY FOR PRINTING:")
    print("   📐 Standard QR code size with text")
    print("   📄 High resolution suitable for printing")
    print("   🎨 Clean black and white design")

if __name__ == "__main__":
    generate_all_qr_codes()
