# Braysint - Construction Materials Website

A modern Django-based bilingual website for Black Rock And Yellow Sands International, selling premium wood, parquet, and plywood materials in both English and Arabic.

## Features

- **Bilingual Support**: Full Arabic and English language support with easy switching
- **Professional Branding**: Custom Braysint logo integrated throughout the site
- **Modern Design**: Clean, professional interface with Bootstrap 5
- **RTL Support**: Proper right-to-left layout for Arabic language
- **Product Management**: Complete product catalog with categories, specifications, and images
- **Search & Filtering**: Advanced search and filtering by wood type, species, and category
- **Responsive Design**: Mobile-friendly layout that works on all devices
- **Admin Interface**: Easy-to-use admin panel for managing products and categories
- **SEO Optimized**: Proper meta tags and URL structure for search engines

## Product Categories

- **Hardwood**: Premium oak, maple, walnut, and more
- **Parquet**: Beautiful flooring solutions
- **Plywood**: Versatile building materials
- **Engineered Wood**: Modern composite solutions

## Technology Stack

- **Backend**: Django 5.2.3
- **Frontend**: Bootstrap 5, Font Awesome, Google Fonts
- **Database**: SQLite (development) - easily configurable for PostgreSQL/MySQL
- **Image Handling**: Pillow for image processing

## Setup Instructions

### 1. Clone or Download the Project
```bash
# Navigate to the project directory
cd construction_materials_site
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
Or run the included script:
```bash
python create_superuser.py
```

### 7. Start Development Server
```bash
python manage.py runserver
```

The website will be available at: http://127.0.0.1:8000/

## Admin Access

- **URL**: http://127.0.0.1:8000/admin/
- **Username**: admin
- **Email**: admin@braysint.com

## Company Information

- **Business Name**: Braysint (Brand)
- **Legal Name**: Black Rock And Yellow Sands International
- **Location**: Sidab, Muscat, Sultanate of Oman
- **Commercial Registration**: 147666
- **VATIN**: OM110034402
- **Business Email**: business@braysint.com
- **Password**: Use the password you created during setup

## Project Structure

```
construction_materials_site/
├── construction_site/          # Main project settings
├── main/                       # Main app (homepage, about, contact)
├── products/                   # Products app (catalog, categories)
├── templates/                  # HTML templates
│   ├── base.html              # Base template with navigation
│   ├── main/                  # Main app templates
│   └── products/              # Product templates
├── static/                    # Static files (CSS, JS, images)
├── media/                     # User-uploaded files
├── venv/                      # Virtual environment
├── db.sqlite3                # Database file
├── manage.py                 # Django management script
└── requirements.txt          # Python dependencies
```

## Key Features Explained

### Product Management
- **Categories**: Organize products into logical groups
- **Specifications**: Detailed product specifications (thickness, width, grade, etc.)
- **Multiple Images**: Support for multiple product images
- **Stock Management**: Track inventory and availability
- **SEO Fields**: Meta descriptions and featured product flags

### Search & Filtering
- **Text Search**: Search by product name, description, or wood species
- **Category Filter**: Filter by product categories
- **Wood Type Filter**: Filter by hardwood, softwood, or engineered
- **Species Filter**: Filter by specific wood species (oak, pine, maple, etc.)
- **Sorting**: Sort by name, price, or date added

### Responsive Design
- **Mobile-First**: Designed for mobile devices first, then desktop
- **Bootstrap 5**: Modern CSS framework for consistent styling
- **Touch-Friendly**: Easy navigation on touch devices
- **Fast Loading**: Optimized images and minimal dependencies

## Adding Content

### Adding Categories
1. Go to Admin Panel → Products → Categories
2. Click "Add Category"
3. Fill in name, slug, description, and optional image
4. Save

### Adding Products
1. Go to Admin Panel → Products → Products
2. Click "Add Product"
3. Fill in basic information (name, category, price, description)
4. Add wood specifications (type, species, dimensions)
5. Set stock information
6. Add images and specifications as needed
7. Save

### Managing Images
- Product images are automatically resized and optimized
- First image marked as "primary" will be used as the main product image
- Add alt text for better SEO and accessibility

### Logo Files
The website uses custom Braysint logos in two sizes:
- **Small Logo**: `static/images/braysint-logo-small.svg` (32px height) - Used in navigation and footer
- **Large Logo**: `static/images/braysint-logo-large.svg` (250px max) - Used in homepage hero section
- Both logos feature the diamond-shaped Braysint branding with gradient colors
- SVG format ensures crisp display on all screen resolutions

## Customization

### Styling
- Main styles are in `templates/base.html` within `<style>` tags
- Colors can be changed by modifying CSS custom properties:
  - `--primary-color`: Main brand color
  - `--secondary-color`: Secondary brand color
  - `--accent-color`: Accent color

### Company Information
- Update company details in `templates/base.html` footer section
- Modify contact information in `templates/main/contact.html`
- Change company story in `templates/main/about.html`

### Navigation
- Main navigation is in `templates/base.html`
- Add/remove menu items as needed

## Multilingual Setup

The website supports both English and Arabic languages with the following features:

### Language Features
- **Language Switcher**: Dropdown in the navigation bar to switch between English/Arabic
- **RTL Support**: Proper right-to-left layout and styling for Arabic
- **URL Patterns**: Language-specific URLs (e.g., `/ar/` for Arabic, `/` for English)
- **Translation Files**: All user-facing text is translatable

### Setting Up Gettext (Windows)

The website uses Django's internationalization framework, which requires gettext tools:

1. **Download and Extract**: Gettext tools are already downloaded in `gettext-tools/` directory
2. **Add to PATH**: Run the included PowerShell script:
   ```powershell
   .\setup_gettext_path.ps1
   ```
3. **Restart Terminal**: Close and reopen your terminal to use the new PATH

### Working with Translations

1. **Update Translations**: When you add new translatable text:
   ```bash
   python manage.py makemessages -l ar
   ```

2. **Edit Translation Files**: Edit `locale/ar/LC_MESSAGES/django.po` to add Arabic translations

3. **Compile Translations**: After editing:
   ```bash
   django-admin compilemessages
   ```

4. **Restart Server**: Restart the development server to see changes

### Adding New Languages

To add support for additional languages:

1. **Update Settings**: Add the language to `LANGUAGES` in `settings.py`
2. **Create Translation Files**: Run `makemessages` for the new language
3. **Translate Content**: Edit the `.po` files with translations
4. **Compile**: Run `compilemessages` to create `.mo` files
5. **Update Templates**: Add the language option to the language switcher

### Current Translations

The website currently includes:
- **English**: Default language, no translation files needed
- **Arabic**: Full translations in `locale/ar/LC_MESSAGES/django.po`

All major sections are translated including:
- Navigation menu
- Homepage content
- Product categories
- Footer information
- Company information

## Production Deployment

For production deployment:

1. **Update Settings**:
   - Set `DEBUG = False`
   - Add your domain to `ALLOWED_HOSTS`
   - Configure proper database (PostgreSQL recommended)
   - Set up static file serving

2. **Environment Variables**:
   - Move sensitive settings to environment variables
   - Use a proper secret key

3. **Static Files**:
   ```bash
   python manage.py collectstatic
   ```

4. **Web Server**:
   - Configure with Gunicorn + Nginx or similar
   - Set up SSL certificate

## Support

For technical support or questions about this Django website, please contact the development team.

## License

This project is created for educational and commercial use. Modify as needed for your business requirements.
#   F o r c e   r e d e p l o y   -   0 7 / 0 8 / 2 0 2 5   2 1 : 5 6 : 2 1  
 