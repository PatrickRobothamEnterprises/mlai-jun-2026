import math

from src.stats import mean, median, stdev


def test_mean_basic():
    assert mean([1, 2, 3, 4]) == 2.5


def test_median_odd_length():
    assert median([3, 1, 2]) == 2
    assert median([5]) == 5


def test_median_even_length():
    # The two middle values (2 and 3) should be averaged -> 2.5
    # This is the failing case described in the seeded issue.
    assert median([1, 2, 3, 4]) == 2.5


def test_median_even_length_unsorted():
    assert median([10, 2, 8, 4]) == 6.0  # sorted -> [2,4,8,10], (4+8)/2


def test_median_empty_raises():
    try:
        median([])
    except ValueError:
        return
    raise AssertionError("median([]) should raise ValueError")


def test_stdev_basic():
    # Sample stdev of [1, 2, 3, 4, 5]: variance = 2.5, sqrt -> ~1.5811
    assert math.isclose(stdev([1, 2, 3, 4, 5]), math.sqrt(2.5))


def test_stdev_identical_values_is_zero():
    assert stdev([7, 7, 7]) == 0.0


def test_stdev_requires_two_values():
    for bad in ([], [42]):
        try:
            stdev(bad)
        except ValueError:
            continue
        raise AssertionError(f"stdev({bad!r}) should raise ValueError")
