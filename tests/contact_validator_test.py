import pytest

from src.contact_validator import (
    is_valid_email,
    is_valid_phone,
    mask_email,
    normalize_phone,
)


def test_is_valid_email_true():
    """A well-formed email should be accepted."""
    assert is_valid_email("student@lpu.in") is True


def test_is_valid_email_false_cases():
    """Malformed email values should be rejected."""
    assert is_valid_email("student.lpu.in") is False
    assert is_valid_email("student@lpu") is False
    assert is_valid_email("student@@lpu.in") is False


def test_is_valid_email_type_error():
    """Non-string inputs should raise TypeError."""
    with pytest.raises(TypeError):
        is_valid_email(12345)


def test_is_valid_phone_true():
    """A well-formed phone number with dashes should be accepted."""
    assert is_valid_phone("555-123-4567") is True


def test_is_valid_phone_false_cases():
    """Malformed phone numbers should be rejected."""
    assert is_valid_phone("555-123-456") is False
    assert is_valid_phone("55512345a") is False
    assert is_valid_phone("123456789") is False


def test_is_valid_phone_type_error():
    """Non-string inputs should raise TypeError."""
    with pytest.raises(TypeError):
        is_valid_phone(1234567890)


def test_mask_email_basic():
    """Typical emails should be masked without changing the domain."""
    assert mask_email("priya@example.com") == "pr***@example.com"


def test_mask_email_short_local():
    """Very short local parts should keep the leading character and mask the rest."""
    assert mask_email("ab@example.com") == "a*@example.com"


def test_mask_email_invalid_raises_value_error():
    """Invalid email input should raise ValueError."""
    with pytest.raises(ValueError):
        mask_email("not-an-email")


def test_normalize_phone():
    """Phone numbers should strip hyphens and keep only digits."""
    assert normalize_phone("555-123-4567") == "5551234567"


def test_normalize_phone_invalid_raises_value_error():
    """Invalid phone numbers should raise ValueError."""
    with pytest.raises(ValueError):
        normalize_phone("12345")
