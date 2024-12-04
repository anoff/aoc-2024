from .solution import is_safe, is_safe_dampened


def test_star1() -> None:
    assert is_safe([7, 6, 4, 2, 1])
    assert not is_safe([1, 2, 7, 8, 9])
    assert not is_safe([9, 7, 6, 2, 1])
    assert not is_safe([8, 6, 4, 4, 1])
    assert not is_safe([8, 6, 4, 5, 3])
    assert is_safe([1, 3, 6, 7, 9])


def test_star2() -> None:
    assert is_safe_dampened([7, 6, 4, 2, 1])
    assert not is_safe_dampened([1, 2, 7, 8, 9])
    assert not is_safe_dampened([9, 7, 6, 2, 1])
    assert is_safe_dampened([8, 6, 4, 4, 1])
    assert is_safe_dampened([8, 6, 4, 5, 3])
    assert is_safe_dampened([1, 3, 2, 4, 5])
    assert is_safe_dampened([1, 3, 6, 7, 9])
