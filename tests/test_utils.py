"""Tests for utils module - some will fail due to bugs."""

import pytest

from src.utils import (
    count_words,
    find_max,
    find_min,
    is_palindrome,
    merge_dicts,
    safe_get,
    truncate_string,
)


class TestFindMax:
    """Tests for find_max function - will expose off-by-one bug."""

    def test_find_max_normal_list(self):
        assert find_max([1, 5, 3, 9, 2]) == 9

    def test_find_max_single_element(self):
        assert find_max([42]) == 42

    def test_find_max_empty_list(self):
        assert find_max([]) is None

    def test_find_max_first_is_largest(self):
        """BUG: This test will FAIL - find_max skips the first element."""
        assert find_max([100, 5, 3, 9, 2]) == 100

    def test_find_max_negative_numbers(self):
        """BUG: This test will FAIL if first element is max."""
        assert find_max([-1, -5, -3, -9, -2]) == -1


class TestFindMin:
    """Tests for find_min function - will expose off-by-one bug."""

    def test_find_min_normal_list(self):
        assert find_min([5, 1, 3, 9, 2]) == 1

    def test_find_min_single_element(self):
        assert find_min([42]) == 42

    def test_find_min_empty_list(self):
        assert find_min([]) is None

    def test_find_min_first_is_smallest(self):
        """BUG: This test will FAIL - find_min skips the first element."""
        assert find_min([0, 5, 3, 9, 2]) == 0


class TestSafeGet:
    """Tests for safe_get function - will expose None dict bug."""

    def test_safe_get_existing_key(self):
        d = {"a": 1, "b": 2}
        assert safe_get(d, "a") == 1

    def test_safe_get_missing_key(self):
        d = {"a": 1}
        assert safe_get(d, "b") is None

    def test_safe_get_with_default(self):
        d = {"a": 1}
        assert safe_get(d, "b", "default") == "default"

    def test_safe_get_none_dict(self):
        """BUG: This test will FAIL - safe_get doesn't handle None dict."""
        result = safe_get(None, "key", "default")
        assert result == "default"


class TestTruncateString:
    """Tests for truncate_string function - will expose ellipsis bug."""

    def test_truncate_short_string(self):
        assert truncate_string("hello", 10) == "hello"

    def test_truncate_exact_length(self):
        assert truncate_string("hello", 5) == "hello"

    def test_truncate_long_string_adds_ellipsis(self):
        """BUG: This test will FAIL - truncate doesn't add ellipsis."""
        result = truncate_string("hello world", 8)
        assert result == "hello..."  # Expected with ellipsis


class TestIsPalindrome:
    """Tests for is_palindrome function - will expose case sensitivity bug."""

    def test_palindrome_simple(self):
        assert is_palindrome("racecar") is True

    def test_palindrome_with_spaces(self):
        assert is_palindrome("a man a plan a canal panama") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_palindrome_mixed_case(self):
        """BUG: This test will FAIL - is_palindrome is case-sensitive."""
        assert is_palindrome("RaceCar") is True


class TestCountWords:
    """Tests for count_words function - will expose multiple spaces bug."""

    def test_count_words_simple(self):
        assert count_words("hello world") == 2

    def test_count_words_single(self):
        assert count_words("hello") == 1

    def test_count_words_empty(self):
        assert count_words("") == 0

    def test_count_words_multiple_spaces(self):
        """BUG: This test will FAIL - count_words doesn't handle multiple spaces."""
        assert count_words("hello  world") == 2  # Two spaces between words


class TestMergeDicts:
    """Tests for merge_dicts function - will expose mutation bug."""

    def test_merge_dicts_simple(self):
        d1 = {"a": 1}
        d2 = {"b": 2}
        result = merge_dicts(d1, d2)
        assert result == {"a": 1, "b": 2}

    def test_merge_dicts_overlap(self):
        d1 = {"a": 1, "b": 2}
        d2 = {"b": 3, "c": 4}
        result = merge_dicts(d1, d2)
        assert result["b"] == 3  # d2 value should win

    def test_merge_dicts_no_mutation(self):
        """BUG: This test will FAIL - merge_dicts mutates dict1."""
        d1 = {"a": 1}
        d2 = {"b": 2}
        d1_original = d1.copy()
        merge_dicts(d1, d2)
        assert d1 == d1_original  # d1 should not be modified
