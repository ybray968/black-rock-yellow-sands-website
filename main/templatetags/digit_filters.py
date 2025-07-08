from django import template
from django.utils.translation import get_language

register = template.Library()

arabic_digits_map = {
    '0': '٠',
    '1': '١',
    '2': '٢',
    '3': '٣',
    '4': '٤',
    '5': '٥',
    '6': '٦',
    '7': '٧',
    '8': '٨',
    '9': '٩'
}

@register.filter
def arabic_digits(value):
    """
    Convert Western digits to Arabic digits if the language is Arabic.
    """
    language = get_language()
    if language == 'ar':
        value = ''.join(arabic_digits_map.get(char, char) for char in str(value))
    return value
