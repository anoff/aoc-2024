from .solution import parse_muls, exec_mul, star1

testin = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


def test_muls() -> None:
    assert parse_muls(testin) == ["mul(2,4)",
                                  "mul(5,5)", "mul(11,8)", "mul(8,5)"]
    assert exec_mul("mul(5,5)") == 25


def test_star1() -> None:
    assert star1(testin) == 161
