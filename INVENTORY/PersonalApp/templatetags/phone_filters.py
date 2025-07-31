from django import template
import re

register = template.Library()


@register.filter
def format_phone(phone_number):
    """
    Format phone number from '0541904705' to '05-41-90-47-05'

    Args:
        phone_number: String or integer phone number

    Returns:
        Formatted phone number string
    """
    if not phone_number:
        return phone_number

    # Convert to string and remove any existing formatting
    phone_str = str(phone_number).replace('-', '').replace(' ', '').replace('(', '').replace(')', '')

    # Remove any non-digit characters except leading +
    phone_str = re.sub(r'[^\d+]', '', phone_str)

    # Handle different phone number formats
    if len(phone_str) == 10 and phone_str.startswith('0'):
        # Format: 0541904705 -> 05-41-90-47-05
        return f"{phone_str[:2]}{phone_str[2:4]} {phone_str[4:6]} {phone_str[6:8]} {phone_str[8:]}"
    elif len(phone_str) == 11 and phone_str.startswith('05'):
        # Handle case where 0 might be missing: 541904705 -> 05-41-90-47-05
        return f"0{phone_str[0]}-{phone_str[1:3]}-{phone_str[3:5]}-{phone_str[5:7]}-{phone_str[7:]}"
    elif len(phone_str) == 9:
        # Handle case where leading 0 is missing: 541904705 -> 05-41-90-47-05
        return f"0{phone_str[0]}-{phone_str[1:3]}-{phone_str[3:5]}-{phone_str[5:7]}-{phone_str[7:]}"

    return phone_number  # Return original if format doesn't match


@register.filter
def format_phone_display(phone_number):
    """
    Alternative formatting for display with parentheses
    Format: 0541904705 -> (054) 190-47-05
    """
    if not phone_number:
        return phone_number

    phone_str = str(phone_number).replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
    phone_str = re.sub(r'[^\d]', '', phone_str)

    if len(phone_str) == 10 and phone_str.startswith('0'):
        return f"({phone_str[:3]}) {phone_str[3:6]}-{phone_str[6:8]}-{phone_str[8:]}"
    elif len(phone_str) == 9:
        return f"(0{phone_str[0:2]}) {phone_str[2:5]}-{phone_str[5:7]}-{phone_str[7:]}"

    return phone_number


@register.filter
def format_phone_international(phone_number, country_code='+972'):
    """
    Format phone number with international country code
    Format: 0541904705 -> +972-54-190-47-05
    """
    if not phone_number:
        return phone_number

    phone_str = str(phone_number).replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
    phone_str = re.sub(r'[^\d]', '', phone_str)

    if len(phone_str) == 10 and phone_str.startswith('0'):
        # Remove leading 0 for international format
        phone_str = phone_str[1:]
        return f"{country_code}-{phone_str[:2]}-{phone_str[2:5]}-{phone_str[5:7]}-{phone_str[7:]}"
    elif len(phone_str) == 9:
        return f"{country_code}-{phone_str[:2]}-{phone_str[2:5]}-{phone_str[5:7]}-{phone_str[7:]}"

    return phone_number