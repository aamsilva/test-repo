"""Utility functions with intentional bugs."""

from typing import Any


def find_max(items: list[Any]) -> Any:
    """Find the maximum value in a list.

    BUG: Off-by-one error - skips the first element!
    """
    if not items:
        return None

    # BUG: Should start from items[0], not items[1]
    max_val = items[1] if len(items) > 1 else items[0]
    for i in range(2, len(items)):
        if items[i] > max_val:
            max_val = items[i]
    return max_val


def find_min(items: list[Any]) -> Any:
    """Find the minimum value in a list.

    BUG: Off-by-one error - skips the first element!
    """
    if not items:
        return None

    # BUG: Should start from items[0], not items[1]
    min_val = items[1] if len(items) > 1 else items[0]
    for i in range(2, len(items)):
        if items[i] < min_val:
            min_val = items[i]
    return min_val


def safe_get(dictionary: dict, key: str, default: Any = None) -> Any:
    """Safely get a value from a dictionary.

    BUG: Doesn't handle None dictionary!
    """
    # BUG: Should check if dictionary is None
    return dictionary.get(key, default)


def truncate_string(text: str, max_length: int) -> str:
    """Truncate a string to max_length characters.

    BUG: Doesn't add ellipsis when truncating!
    """
    if len(text) <= max_length:
        return text
    # BUG: Should add "..." when truncating
    return text[:max_length]


def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome.

    BUG: Case-sensitive comparison!
    """
    # BUG: Should be case-insensitive
    cleaned = "".join(c for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


def count_words(text: str) -> int:
    """Count the number of words in a text.

    BUG: Doesn't handle multiple spaces correctly!
    """
    if not text:
        return 0
    # BUG: Multiple spaces will create empty strings
    return len(text.split(" "))


def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """Merge two dictionaries.

    BUG: Modifies dict1 in place instead of creating a new dict!
    """
    # BUG: Should create a new dict to avoid side effects
    dict1.update(dict2)
    return dict1
