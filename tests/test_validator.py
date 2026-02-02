"""Tests for validator module - some will fail due to bugs."""

import pytest

from src.validator import (
    sanitize_input,
    validate_age,
    validate_email,
    validate_password,
    validate_phone,
    validate_url,
)


class TestValidateEmail:
    """Tests for validate_email function - will expose regex bug."""

    def test_valid_email(self):
        assert validate_email("user@example.com") is True

    def test_valid_email_with_subdomain(self):
        assert validate_email("user@mail.example.com") is True

    def test_empty_email(self):
        assert validate_email("") is False

    def test_invalid_email_no_domain(self):
        """BUG: This test will FAIL - regex is too permissive."""
        assert validate_email("user@") is False

    def test_invalid_email_no_user(self):
        """BUG: This test will FAIL - regex is too permissive."""
        assert validate_email("@example.com") is False


class TestValidatePhone:
    """Tests for validate_phone function - will expose formatting bug."""

    def test_valid_phone_digits_only(self):
        assert validate_phone("1234567890") is True

    def test_phone_too_short(self):
        assert validate_phone("123456789") is False

    def test_phone_too_long(self):
        assert validate_phone("12345678901") is False

    def test_phone_with_dashes(self):
        """BUG: This test will FAIL - phone doesn't strip formatting."""
        assert validate_phone("123-456-7890") is True

    def test_phone_with_parentheses(self):
        """BUG: This test will FAIL - phone doesn't strip formatting."""
        assert validate_phone("(123) 456-7890") is True


class TestValidatePassword:
    """Tests for validate_password function - will expose special char bug."""

    def test_valid_password(self):
        is_valid, error = validate_password("Password1")
        assert is_valid is True
        assert error is None

    def test_password_too_short(self):
        is_valid, error = validate_password("Pass1")
        assert is_valid is False
        assert "8 characters" in error

    def test_password_no_uppercase(self):
        is_valid, error = validate_password("password1")
        assert is_valid is False
        assert "uppercase" in error

    def test_password_no_digit(self):
        is_valid, error = validate_password("Password")
        assert is_valid is False
        assert "digit" in error

    def test_password_requires_special_char(self):
        """BUG: This test will FAIL - password doesn't check for special chars."""
        is_valid, error = validate_password("Password1")
        # A strong password should require special characters
        assert is_valid is False or "special" in str(error).lower()


class TestValidateUrl:
    """Tests for validate_url function - will expose structure bug."""

    def test_valid_http_url(self):
        assert validate_url("http://example.com") is True

    def test_valid_https_url(self):
        assert validate_url("https://example.com") is True

    def test_empty_url(self):
        assert validate_url("") is False

    def test_invalid_url_no_host(self):
        """BUG: This test will FAIL - URL validation is too simple."""
        assert validate_url("http://") is False

    def test_invalid_url_no_protocol(self):
        assert validate_url("example.com") is False


class TestValidateAge:
    """Tests for validate_age function - will expose upper bound bug."""

    def test_valid_age(self):
        is_valid, error = validate_age(25)
        assert is_valid is True

    def test_age_zero(self):
        is_valid, error = validate_age(0)
        assert is_valid is True

    def test_negative_age(self):
        is_valid, error = validate_age(-5)
        assert is_valid is False

    def test_unrealistic_age_boundary(self):
        """BUG: This test will FAIL - upper bound is too high (200)."""
        # 150 years old is unrealistic but currently passes
        is_valid, error = validate_age(150)
        assert is_valid is False


class TestSanitizeInput:
    """Tests for sanitize_input function - will expose encoding bug."""

    def test_sanitize_removes_lt(self):
        assert "&lt;" in sanitize_input("<script>")

    def test_sanitize_removes_gt(self):
        assert "&gt;" in sanitize_input("</script>")

    def test_sanitize_empty(self):
        assert sanitize_input("") == ""

    def test_sanitize_quotes(self):
        """BUG: This test will FAIL - sanitize doesn't encode quotes."""
        result = sanitize_input('onclick="alert(1)"')
        assert '"' not in result or "&quot;" in result

    def test_sanitize_single_quotes(self):
        """BUG: This test will FAIL - sanitize doesn't encode single quotes."""
        result = sanitize_input("onclick='alert(1)'")
        assert "'" not in result or "&#39;" in result
