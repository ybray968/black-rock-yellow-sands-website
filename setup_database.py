#!/usr/bin/env python
"""
Script to set up database with thickness specifications for production deployment.
This ensures that thickness specifications are always present for the three key products.
"""
import os
import django
import subprocess
import sys

def setup_database():
    """Set up the database with required thickness specifications."""
    print("🔧 Setting up database for production...")
    
    # Set up Django environment
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings_production')
    django.setup()
    
    # Run migrations first
    print("📋 Running migrations...")
    subprocess.run([sys.executable, 'manage.py', 'migrate'], check=True)
    
    # Add thickness specifications
    print("📦 Adding thickness specifications...")
    subprocess.run([sys.executable, 'manage.py', 'add_thickness_specs'], check=True)
    
    print("✅ Database setup complete!")

if __name__ == '__main__':
    setup_database()
