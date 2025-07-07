"""
Custom Security Middleware for Enhanced Protection
This middleware provides additional security layers beyond Django's built-in protections.
"""

import re
import logging
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.core.exceptions import SuspiciousOperation
from django.conf import settings

logger = logging.getLogger('django.security')


class SecurityMiddleware:
    """
    Enhanced security middleware to protect against various attacks
    """
    
    # Patterns that might indicate SQL injection attempts
    SQL_INJECTION_PATTERNS = [
        r"(\b(select|insert|update|delete|drop|create|alter|exec|execute|union|script)\b)",
        r"(\b(or|and)\s+\d+\s*=\s*\d+)",
        r"(--|\/\*|\*\/)",
        r"(\bor\b\s+\btrue\b|\bor\b\s+\bfalse\b)",
        r"(\'\s*(or|and)\s*\'\w*\'\s*=\s*\'\w*)",
        r"(\bunion\b.*\bselect\b)",
        r"(\bselect\b.*\bfrom\b.*\bwhere\b)",
    ]
    
    # Patterns that might indicate XSS attempts
    XSS_PATTERNS = [
        r"<script[^>]*>.*?</script>",
        r"javascript\s*:",
        r"on\w+\s*=",
        r"<iframe[^>]*>.*?</iframe>",
        r"<object[^>]*>.*?</object>",
        r"<embed[^>]*>.*?</embed>",
        r"<link[^>]*>",
        r"<meta[^>]*>",
        r"vbscript\s*:",
        r"data\s*:\s*text/html",
    ]
    
    # Patterns for path traversal attempts
    PATH_TRAVERSAL_PATTERNS = [
        r"\.\./",
        r"\.\.\\",
        r"%2e%2e%2f",
        r"%2e%2e\\",
        r"\.\.%2f",
        r"\.\.%5c",
    ]
    
    # Suspicious headers or values
    SUSPICIOUS_PATTERNS = [
        r"<\?php",
        r"<%.*%>",
        r"\${.*}",
        r"{{.*}}",
        r"\[.*\]",
    ]
    
    # Rate limiting - simple in-memory store (use Redis in production)
    request_counts = {}
    
    def __init__(self, get_response):
        self.get_response = get_response
        
        # Compile regex patterns for better performance
        self.sql_regex = [re.compile(pattern, re.IGNORECASE) for pattern in self.SQL_INJECTION_PATTERNS]
        self.xss_regex = [re.compile(pattern, re.IGNORECASE) for pattern in self.XSS_PATTERNS]
        self.path_regex = [re.compile(pattern, re.IGNORECASE) for pattern in self.PATH_TRAVERSAL_PATTERNS]
        self.suspicious_regex = [re.compile(pattern, re.IGNORECASE) for pattern in self.SUSPICIOUS_PATTERNS]
    
    def __call__(self, request):
        """
        Process the request and response
        """
        # Security checks before processing request
        security_response = self.process_request_security(request)
        if security_response:
            return security_response
        
        # Process the request
        response = self.get_response(request)
        
        # Add security headers to response
        response = self.process_response(request, response)
        
        return response
    
    def process_request_security(self, request):
        """
        Process incoming requests for security threats
        """
        
        # Get client IP
        client_ip = self.get_client_ip(request)
        
        # Basic rate limiting (100 requests per minute per IP)
        if self.is_rate_limited(client_ip):
            logger.warning(f"Rate limit exceeded for IP: {client_ip}")
            return HttpResponseForbidden("Rate limit exceeded")
        
        # Check for suspicious headers
        if self.has_suspicious_headers(request):
            logger.warning(f"Suspicious headers detected from IP: {client_ip}")
            return HttpResponseBadRequest("Invalid request headers")
        
        # Check request path for traversal attempts
        if self.has_path_traversal(request.path):
            logger.warning(f"Path traversal attempt detected: {request.path} from IP: {client_ip}")
            raise SuspiciousOperation("Path traversal attempt detected")
        
        # Check query parameters and POST data
        if self.has_malicious_content(request):
            logger.warning(f"Malicious content detected from IP: {client_ip}")
            return HttpResponseBadRequest("Invalid request content")
        
        return None
    
    def get_client_ip(self, request):
        """
        Get the real client IP address
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    def is_rate_limited(self, ip):
        """
        Simple rate limiting implementation
        """
        import time
        current_time = int(time.time())
        minute_window = current_time // 60
        
        key = f"{ip}_{minute_window}"
        
        if key in self.request_counts:
            if self.request_counts[key] >= 100:  # 100 requests per minute
                return True
            self.request_counts[key] += 1
        else:
            self.request_counts[key] = 1
            
        # Clean old entries (keep only current and previous minute)
        keys_to_remove = [k for k in self.request_counts.keys() 
                         if int(k.split('_')[1]) < minute_window - 1]
        for key in keys_to_remove:
            del self.request_counts[key]
            
        return False
    
    def has_suspicious_headers(self, request):
        """
        Check for suspicious headers that might indicate an attack
        """
        suspicious_headers = [
            'HTTP_X_REQUESTED_WITH',
            'HTTP_USER_AGENT',
            'HTTP_REFERER',
        ]
        
        for header in suspicious_headers:
            value = request.META.get(header, '')
            if value:
                # Check for extremely long headers (possible buffer overflow)
                if len(value) > 1000:
                    return True
                
                # Check for suspicious patterns in headers
                for regex in self.suspicious_regex:
                    if regex.search(value):
                        return True
        
        return False
    
    def has_path_traversal(self, path):
        """
        Check for path traversal attempts
        """
        for regex in self.path_regex:
            if regex.search(path):
                return True
        return False
    
    def has_malicious_content(self, request):
        """
        Check request content for SQL injection, XSS, and other attacks
        """
        # Check GET parameters
        for key, value in request.GET.items():
            if self.is_malicious_string(value) or self.is_malicious_string(key):
                return True
        
        # Check POST data
        if hasattr(request, 'POST'):
            for key, value in request.POST.items():
                if self.is_malicious_string(value) or self.is_malicious_string(key):
                    return True
        
        return False
    
    def is_malicious_string(self, text):
        """
        Check if a string contains malicious patterns
        """
        if not isinstance(text, str):
            text = str(text)
        
        # Check for SQL injection
        for regex in self.sql_regex:
            if regex.search(text):
                return True
        
        # Check for XSS
        for regex in self.xss_regex:
            if regex.search(text):
                return True
        
        # Check for other suspicious patterns
        for regex in self.suspicious_regex:
            if regex.search(text):
                return True
        
        return False
    
    def process_response(self, request, response):
        """
        Add additional security headers to responses
        """
        # Additional security headers
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['X-XSS-Protection'] = '1; mode=block'
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        response['Content-Security-Policy'] = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://cdnjs.cloudflare.com; "
            "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://cdnjs.cloudflare.com https://fonts.googleapis.com; "
            "font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com; "
            "img-src 'self' data:; "
            "connect-src 'self'; "
            "frame-ancestors 'none'; "
            "base-uri 'self'; "
            "form-action 'self';"
        )
        
        return response


class AdminSecurityMiddleware:
    """
    Additional security for admin interface
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        """
        Process the request and response
        """
        # Security checks for admin interface
        if request.path.startswith('/admin/'):
            # Additional checks for admin interface
            
            # Check if accessing admin from allowed IPs (configure in production)
            # ADMIN_ALLOWED_IPS = getattr(settings, 'ADMIN_ALLOWED_IPS', [])
            # if ADMIN_ALLOWED_IPS:
            #     client_ip = self.get_client_ip(request)
            #     if client_ip not in ADMIN_ALLOWED_IPS:
            #         return HttpResponseForbidden("Access denied")
            
            # Log admin access attempts
            logger.info(f"Admin access attempt from {self.get_client_ip(request)} to {request.path}")
        
        # Process the request
        response = self.get_response(request)
        return response
    
    def get_client_ip(self, request):
        """Get client IP address"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
