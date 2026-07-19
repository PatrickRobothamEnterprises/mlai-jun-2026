"""Tiny statistics helpers.

Used in the MLAI talk demo. Intentionally contains ONE clear bug in
`median()` so an agent can read the issue, fix it, and prove the fix with tests.
"""

from typing import Sequence


def mean(values: Sequence[float]) -> float:
    """Arithmetic mean of a non-empty sequence."""
    if not values:
        raise ValueError("mean() requires at least one value")
    return sum(values) / len(values)


def median(values: Sequence[float]) -> float:
    """Return the median of a sequence.

    BUG: for even-length inputs this returns the lower of the two middle
    elements instead of averaging the two middle elements.
    """
    if not values:
        raise ValueError("median() requires at least one value")
    ordered = sorted(values)
    mid = len(ordered) // 2
    return ordered[mid - 1] if len(ordered) % 2 == 0 else ordered[mid]
