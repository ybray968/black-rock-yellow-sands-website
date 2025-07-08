#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from django.test import RequestFactory
from django.urls import reverse
from django.utils import translation
from django.conf import settings

def test_language_switching():
    """Test language switching URLs"""
    
    factory = RequestFactory()
    
    # Test URLs with different language prefixes
    test_paths = [
        '/',
        '/products/',
        '/about/',
        '/contact/',
        '/ar/',
        '/ar/products/',
        '/ar/about/',
        '/ar/contact/',
    ]
    
    print("Testing URL path transformations:")
    print("="*50)
    
    for path in test_paths:
        print(f"Original path: {path}")
        
        # Simulate what the template filter does
        if path.startswith('/ar'):
            next_url = path[3:] or '/'
        elif path.startswith('/en'):
            next_url = path[3:] or '/'
        else:
            next_url = path
            
        print(f"Next URL would be: {next_url}")
        print("-" * 30)

if __name__ == '__main__':
    test_language_switching()
