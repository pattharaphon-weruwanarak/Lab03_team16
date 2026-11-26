def reverse_words(text: str) -> str:
    """Return the words in reverse order, separated by single spaces."""
    return " ".join(reversed(text.split()))
