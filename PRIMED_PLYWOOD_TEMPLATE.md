# Primed Plywood Product Template

## Product Structure Reference
This document serves as a reference template for future products based on the Primed Plywood implementation.

### Product Details
- **Name**: "Primed Plywood" (keep product name in English in Arabic description)
- **Category**: Plywood
- **Wood Species**: birch
- **Wood Type**: engineered (film_faced for plywood products)
- **Featured**: True
- **In Stock**: True

### Description Pattern
**English**: Technical description focusing on:
- Material composition (birch plywood + coating type)
- Surface preparation purpose
- Usage scope (indoor/outdoor)
- Environmental compatibility
- Color/appearance features
- Application benefits

**Arabic**: Direct translation keeping product name in English as requested

### Specifications Structure
1. **Thicknesses, mm** / **السماكات، مم**
   - Range format: "6.5, 9, 12, 15, 18, 19, 21, 24, 27, 30, 35, 40"

2. **Sizes, mm** / **الأحجام، مم**
   - Multiple size options with "cut-to-size" option

3. **Grades** / **الدرجات**
   - Format: "1/1 (B/B)" style notation

4. **Type of surface** / **نوع السطح**
   - Format: "smooth/smooth (F/F)" style notation

5. **Film density, g/m²** / **كثافة الفيلم، غ/م²**
   - Multiple density options: "140, 220"

6. **Formaldehyde emission (limit value 3.5 mg/h x m²)** / **انبعاث الفورمالديهايد (القيمة الحدية 3.5 مغ/ساعة × م²)**
   - Low emission range: "0.1-0.3 mg/h x m²"

### Advantages Template (for product_list.html)
Four advantages with appropriate icons:

1. **Perfect surface for [specific use]** (🎨 fas fa-paint-brush)
   - Subtitle explaining the base/foundation benefit

2. **Saving time and [materials]** (⏰ fas fa-clock)
   - Subtitle about preparation work reduction

3. **[Resistance/durability feature]** (🛡️ fas fa-shield-alt)
   - Subtitle about coating/surface properties

4. **Easy [process] without [requirement]** (✨ fas fa-magic)
   - Subtitle about treatment requirements

### Image Mapping
- Home template: `plywood-primed.png`
- Product list template: `plywood-primed.png`
- Application image: `primed-plywood-application.png`

### Database Fields Used
- `name` (English)
- `name_ar` (Arabic - usually same as English for product names)
- `description` (English)
- `description_ar` (Arabic)
- `category` (ForeignKey to Category)
- `wood_species` (CharField choice)
- `wood_type` (CharField choice)
- `featured` (Boolean)
- `in_stock` (Boolean)
- `specifications` (Related ProductSpecification objects)

### Template Integration Points
1. **Home template**: Image mapping in featured products section
2. **Product list template**: 
   - Image mapping for product display
   - Advantages section with icons
   - Specifications display
3. **Translation considerations**: Product names stay in English, descriptions translated

This template can be used for future products with similar structure and formatting requirements.
