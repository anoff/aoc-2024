from .solution import star1, star2, get_neighbors

testin = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split("\n")


def test_neighbors() -> None:
    assert len(get_neighbors(0, 0, testin)) == 3
    assert len(get_neighbors(2, 2, testin)) == 8
    assert len(get_neighbors(0, 2, testin)) == 5
    assert len(get_neighbors(9, 0, testin)) == 3


def test_star1() -> None:
    assert star1(testin) == 18


def test_star2() -> None:
    assert star2()
