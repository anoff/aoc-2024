from solution import get_diff, get_similarity

testinput = """
3   4
4   3
2   5
1   3
3   9
3   3
"""


def test_get_diff() -> None:
    assert get_diff(sorted([3, 4, 2, 1, 3, 3]),
                    sorted([4, 3, 5, 3, 9, 3])) == 11


def test_get_similarity() -> None:
    assert get_similarity([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]) == 31
