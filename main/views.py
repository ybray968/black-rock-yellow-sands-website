from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext as _
from products.models import Product, Category
import logging

def home(request):
    """Homepage view"""
    # Use same custom ordering as products page
    from django.db.models import Case, When, IntegerField, Value
    
    featured_products = Product.objects.filter(featured=True, in_stock=True).annotate(
        custom_order=Case(
            When(name__icontains='Deck', then=Value(1)),
            When(name__icontains='Exterior Birch', then=Value(2)),
            When(name__icontains='Interior Birch', then=Value(3)),
            When(name__icontains='Birch Interior', then=Value(3)),
            When(name__icontains='Parquet', then=Value(4)),
            When(name__icontains='Antislip MT', then=Value(5)),
            When(name__icontains='Antislip Wire', then=Value(5)),
            default=Value(6),
            output_field=IntegerField()
        )
    ).order_by('custom_order', 'name')[:6]
    
    categories = Category.objects.all()[:4]
    
    context = {
        'featured_products': featured_products,
        'categories': categories,
    }
    return render(request, 'main/home.html', context)

def about(request):
    """About page view"""
    return render(request, 'main/about.html')

def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        company = request.POST.get('company', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        human_verification = request.POST.get('human_verification')
        
        # Basic validation
        if not name or not email or not subject or not message:
            context = {
                'error': 'Please fill in all required fields.',
                'form_data': request.POST
            }
            return render(request, 'main/contact.html', context)
        
        if not human_verification:
            context = {
                'error': 'Please verify that you are human.',
                'form_data': request.POST
            }
            return render(request, 'main/contact.html', context)
        
        # Send email
        try:
            logging.info(f"Attempting to send email with backend: {settings.EMAIL_BACKEND}")
            logging.info(f"Email host: {getattr(settings, 'EMAIL_HOST', 'Not set')}")
            logging.info(f"Email from: {settings.DEFAULT_FROM_EMAIL}")
            logging.info(f"Email to: {settings.CONTACT_EMAIL}")
            
            from_email = getattr(settings, 'EMAIL_HOST_USER', 'finance@braysint.com')
            send_mail(
                subject=f"Contact Form - {subject}",
                message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nCompany: {company}\nMessage: {message}",
                from_email=from_email,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            logging.info("Email sent successfully")
            context = {
                'success': _('Thank you for your message! We will get back to you soon.'),
            }
        except Exception as e:
            logging.error(f"Error sending email: {e}")
            context = {
                'error': _('There was an issue sending your message. Please try again later.'),
                'form_data': request.POST
            }
        
        return render(request, 'main/contact.html', context)
    
    return render(request, 'main/contact.html')

def health_check(request):
    """Health check endpoint for deployment platforms"""
    return JsonResponse({'status': 'healthy', 'message': 'Application is running'})
