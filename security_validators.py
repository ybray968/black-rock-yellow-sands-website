"""
Security Validators for Form Inputs and User Data
This module provides validators to prevent malicious input in forms.
"""

import re
import html
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class SecurityValidator:
    """
    Base security validator class
    """
    
    # Common malicious patterns
    SQL_PATTERNS = [
        r"(\bselect\b|\binsert\b|\bupdate\b|\bdelete\b|\bdrop\b|\bcreate\b|\balter\b)",
        r"(\bunion\b.*\bselect\b)",
        r"(\bor\b\s+\d+\s*=\s*\d+)",
        r"(--|\/\*|\*\/)",
        r"(\'\s*(or|and)\s*\')",
    ]
    
    XSS_PATTERNS = [
        r"<script[^>]*>.*?</script>",
        r"javascript\s*:",
        r"on\w+\s*=",
        r"<iframe[^>]*>",
        r"<object[^>]*>",
        r"<embed[^>]*>",
        r"vbscript\s*:",
        r"data\s*:\s*text/html",
    ]
    
    def __init__(self):
        # Compile patterns for better performance
        self.sql_regex = [re.compile(pattern, re.IGNORECASE) for pattern in self.SQL_PATTERNS]
        self.xss_regex = [re.compile(pattern, re.IGNORECASE) for pattern in self.XSS_PATTERNS]
    
    def validate_sql_injection(self, value):
        """Check for SQL injection patterns"""
        if not isinstance(value, str):
            value = str(value)
        
        for regex in self.sql_regex:
            if regex.search(value):
                raise ValidationError(
                    _('Invalid input detected. Please remove any special SQL characters.'),
                    code='sql_injection'
                )
    
    def validate_xss(self, value):
        """Check for XSS patterns"""
        if not isinstance(value, str):
            value = str(value)
        
        for regex in self.xss_regex:
            if regex.search(value):
                raise ValidationError(
                    _('Invalid input detected. HTML/JavaScript content is not allowed.'),
                    code='xss_attempt'
                )
    
    def validate_length(self, value, max_length=1000):
        """Validate input length to prevent buffer overflow"""
        if len(str(value)) > max_length:
            raise ValidationError(
                _('Input too long. Maximum %(max_length)d characters allowed.'),
                params={'max_length': max_length},
                code='input_too_long'
            )
    
    def sanitize_input(self, value):
        """Sanitize input by escaping HTML entities"""
        if isinstance(value, str):
            return html.escape(value)
        return value


def validate_safe_text(value):
    """
    Validator function for text fields that should be safe from XSS and SQL injection
    """
    validator = SecurityValidator()
    validator.validate_sql_injection(value)
    validator.validate_xss(value)
    validator.validate_length(value, 1000)
    return True


def validate_safe_name(value):
    """
    Validator for name fields (stricter validation)
    """
    validator = SecurityValidator()
    validator.validate_sql_injection(value)
    validator.validate_xss(value)
    validator.validate_length(value, 100)
    
    # Additional name-specific validation
    if not re.match(r'^[a-zA-Z\s\-\'\.]+$', value):
        raise ValidationError(
            _('Name can only contain letters, spaces, hyphens, apostrophes, and periods.'),
            code='invalid_name_format'
        )
    
    return True


def validate_safe_email(value):
    """
    Enhanced email validation
    """
    validator = SecurityValidator()
    validator.validate_sql_injection(value)
    validator.validate_xss(value)
    validator.validate_length(value, 254)  # RFC standard max email length
    
    # Basic email format check
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, value):
        raise ValidationError(
            _('Please enter a valid email address.'),
            code='invalid_email_format'
        )
    
    return True


def validate_phone_number(value):
    """
    Validate phone number format
    """
    validator = SecurityValidator()
    validator.validate_sql_injection(value)
    validator.validate_xss(value)
    validator.validate_length(value, 20)
    
    # Clean phone number (remove spaces, dashes, parentheses)
    cleaned = re.sub(r'[\s\-\(\)]+', '', value)
    
    # Check if it contains only digits and optional + at the start
    if not re.match(r'^\+?[0-9]+$', cleaned):
        raise ValidationError(
            _('Please enter a valid phone number with only digits, spaces, dashes, and parentheses.'),
            code='invalid_phone_format'
        )
    
    return True


def validate_company_name(value):
    """
    Validate company name
    """
    validator = SecurityValidator()
    validator.validate_sql_injection(value)
    validator.validate_xss(value)
    validator.validate_length(value, 200)
    
    # Allow letters, numbers, spaces, and common business punctuation
    if not re.match(r'^[a-zA-Z0-9\s\-\&\.\,\'\"]+$', value):
        raise ValidationError(
            _('Company name contains invalid characters.'),
            code='invalid_company_format'
        )
    
    return True


def validate_no_links(value):
    """
    Validate that the input doesn't contain any URLs or links
    """
    if not isinstance(value, str):
        value = str(value)
    
    # Patterns to detect URLs and links
    url_patterns = [
        r'https?://[^\s]+',
        r'www\.[^\s]+',
        r'[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]\.(com|org|net|gov|edu|co|uk|de|fr|it|es|ru|cn|jp|au|ca|br|in)\b',
        r'\b\w+\.(com|org|net|gov|edu|co|uk|de|fr|it|es|ru|cn|jp|au|ca|br|in)\b',
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    ]
    
    for pattern in url_patterns:
        if re.search(pattern, value, re.IGNORECASE):
            raise ValidationError(
                _('Links, URLs, and email addresses are not allowed in this field.'),
                code='links_not_allowed'
            )
    
    return True


def validate_message_content(value):
    """
    Validate message content (most permissive but still secure)
    """
    validator = SecurityValidator()
    validator.validate_sql_injection(value)
    validator.validate_xss(value)
    validator.validate_length(value, 1000)
    
    # Check for links and URLs
    validate_no_links(value)
    
    # Check for excessive repetition (possible spam)
    if len(set(value.lower().split())) < len(value.split()) / 3:
        raise ValidationError(
            _('Message appears to contain excessive repetition.'),
            code='excessive_repetition'
        )
    
    return True


class SecureFormMixin:
    """
    Mixin for forms to add security validation
    """
    
    def clean(self):
        """
        Apply security validation to all form fields
        """
        cleaned_data = super().clean()
        validator = SecurityValidator()
        
        for field_name, value in cleaned_data.items():
            if isinstance(value, str) and value:
                try:
                    # Apply basic security validation to all text fields
                    validator.validate_sql_injection(value)
                    validator.validate_xss(value)
                    
                    # Sanitize the input
                    cleaned_data[field_name] = validator.sanitize_input(value)
                    
                except ValidationError as e:
                    self.add_error(field_name, e)
        
        return cleaned_data


# Custom field types with built-in security
from django import forms


class SecureCharField(forms.CharField):
    """
    CharField with built-in security validation
    """
    
    def __init__(self, *args, **kwargs):
        self.security_validator = SecurityValidator()
        super().__init__(*args, **kwargs)
    
    def validate(self, value):
        super().validate(value)
        if value:
            self.security_validator.validate_sql_injection(value)
            self.security_validator.validate_xss(value)
    
    def clean(self, value):
        value = super().clean(value)
        if value:
            return self.security_validator.sanitize_input(value)
        return value


class SecureTextField(forms.CharField):
    """
    TextField with built-in security validation
    """
    
    def __init__(self, *args, **kwargs):
        self.security_validator = SecurityValidator()
        kwargs.setdefault('widget', forms.Textarea)
        super().__init__(*args, **kwargs)
    
    def validate(self, value):
        super().validate(value)
        if value:
            self.security_validator.validate_sql_injection(value)
            self.security_validator.validate_xss(value)
            self.security_validator.validate_length(value, 1000)
    
    def clean(self, value):
        value = super().clean(value)
        if value:
            return self.security_validator.sanitize_input(value)
        return value


class SecureEmailField(forms.EmailField):
    """
    EmailField with enhanced security validation
    """
    
    def __init__(self, *args, **kwargs):
        self.security_validator = SecurityValidator()
        super().__init__(*args, **kwargs)
    
    def validate(self, value):
        super().validate(value)
        if value:
            validate_safe_email(value)
    
    def clean(self, value):
        value = super().clean(value)
        if value:
            return self.security_validator.sanitize_input(value)
        return value
