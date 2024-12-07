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


def test_star1() -> None:
    assert star1(testin) == 18


def test_star2() -> None:
    assert star2()
