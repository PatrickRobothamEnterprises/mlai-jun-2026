from src.stats import mean, median


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
