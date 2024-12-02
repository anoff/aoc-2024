from .solution import get_diff, get_similarity

testinput = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

def test_get_diff() -> None:
    assert get_diff(testinput) == 11


def test_get_similarity() -> None:
    assert get_similarity(testinput) == 31