"""Input validation utilities with bugs."""

import re
from typing import Optional


def validate_email(email: str) -> bool:
    """Validate an email address.

    BUG: Regex is too permissive!
    """
    if not email:
        return False
    # BUG: This regex allows invalid emails like "test@" or "@domain.com"
    pattern = r".+@.+"
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Validate a phone number (US format).

    BUG: Doesn't strip non-digit characters before validation!
    """
    if not phone:
        return False
    # BUG: Should strip dashes, spaces, parentheses first
    return len(phone) == 10 and phone.isdigit()


def validate_password(password: str) -> tuple[bool, Optional[str]]:
    """Validate password strength.

    Returns (is_valid, error_message).

    BUG: Doesn't check for special characters!
    """
    if not password:
        return False, "Password cannot be empty"

    if len(password) < 8:
        return False, "Password must be at least 8 characters"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)

    if not has_upper:
        return False, "Password must contain an uppercase letter"
    if not has_lower:
        return False, "Password must contain a lowercase letter"
    if not has_digit:
        return False, "Password must contain a digit"

    # BUG: Should also check for special characters
    return True, None


def validate_url(url: str) -> bool:
    """Validate a URL.

    BUG: Doesn't properly validate URL structure!
    """
    if not url:
        return False
    # BUG: This is too simple, allows invalid URLs
    return url.startswith("http://") or url.startswith("https://")


def validate_age(age: int) -> tuple[bool, Optional[str]]:
    """Validate age is reasonable.

    BUG: Upper bound is too high!
    """
    if age < 0:
        return False, "Age cannot be negative"
    # BUG: 200 is not a reasonable max age, should be ~120-130
    if age > 200:
        return False, "Age seems unrealistic"
    return True, None


def sanitize_input(text: str) -> str:
    """Sanitize user input to prevent XSS.

    BUG: Incomplete HTML entity encoding!
    """
    if not text:
        return ""
    # BUG: Missing many dangerous characters like ', ", etc.
    return text.replace("<", "&lt;").replace(">", "&gt;")
