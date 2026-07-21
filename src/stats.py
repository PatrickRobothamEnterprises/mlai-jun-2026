"""Tiny statistics helpers.

Used in the MLAI talk demo. Intentionally contains ONE clear bug in
`median()` so an agent can read the issue, fix it, and prove the fix with tests.
"""

from math import sqrt
from typing import Sequence


def mean(values: Sequence[float]) -> float:
    """Arithmetic mean of a non-empty sequence."""
    if not values:
        raise ValueError("mean() requires at least one value")
    return sum(values) / len(values)


def median(values: Sequence[float]) -> float:
    """Return the median of a sequence.

    For odd-length inputs this is the middle element; for even-length inputs
    it is the average of the two middle elements.
    """
    if not values:
        raise ValueError("median() requires at least one value")
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2 == 0:
        return (ordered[mid - 1] + ordered[mid]) / 2
    return ordered[mid]


def stdev(values: Sequence[float]) -> float:
    """Return the sample standard deviation of a sequence.

    Uses Bessel's correction (dividing by ``n - 1``), matching
    :func:`statistics.stdev`. Requires at least two values.
    """
    n = len(values)
    if n < 2:
        raise ValueError("stdev() requires at least two values")
    avg = mean(values)
    variance = sum((x - avg) ** 2 for x in values) / (n - 1)
    return sqrt(variance)
