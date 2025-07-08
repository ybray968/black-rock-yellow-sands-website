# Template filter to convert numbers to Arabic digits
from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter(name='to_arabic_digits')
def to_arabic_digits(value):
    """
    Convert English digits in a string to Arabic digits intelligently.
    Preserves technical codes and converts measurements, dimensions, etc.
    """
    if not value:
        return value
    
    value = str(value)
    
    # English to Arabic digit mapping
    digit_map = {
        '0': '٠', '1': '١', '2': '٢', '3': '٣', '4': '٤',
        '5': '٥', '6': '٦', '7': '٧', '8': '٨', '9': '٩'
    }
    
    # Convert standalone numbers and measurements
    # Pattern for numbers that should be converted:
    # - Standalone numbers
    # - Numbers with units (mm, m², g/m², etc.)
    # - Dimensions (1220x2440)
    # - Ranges (6-12, 0.1-0.3)
    
    def convert_number(match):
        number = match.group(0)
        # Convert each digit
        converted = ''
        for char in number:
            if char in digit_map:
                converted += digit_map[char]
            else:
                converted += char
        return converted
    
    # Patterns to convert:
    patterns = [
        # Standalone numbers at word boundaries
        r'\b\d+\b',
        # Numbers with units (mm, m², g/m², etc.)
        r'\d+(?:[.,]\d+)?\s*(?:mm|cm|m²|m|g/m²|kg|%)',
        # Dimensions (1220x2440, 1500x1500)
        r'\d+x\d+',
        # Ranges (6-12, 0.1-0.3)
        r'\d+(?:[.,]\d+)?[-–]\d+(?:[.,]\d+)?',
        # Numbers with decimal points or commas
        r'\d+[.,]\d+',
        # Numbers in parentheses when standalone
        r'\(\d+\)',
    ]
    
    # Apply conversion for each pattern
    result = value
    for pattern in patterns:
        result = re.sub(pattern, convert_number, result)
    
    return mark_safe(result)

@register.filter(name='to_arabic_digits_if_arabic')
def to_arabic_digits_if_arabic(value, language_code='en'):
    """
    Convert to Arabic digits only if the language is Arabic
    """
    if language_code == 'ar':
        return to_arabic_digits(value)
    return value
