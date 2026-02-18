"""Tests for vigenere."""

import pytest
from vigenere import vigenere


class TestVigenere:
    """Test suite for vigenere."""

    def test_basic(self):
        """Test basic usage."""
        result = vigenere("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            vigenere("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = vigenere(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
