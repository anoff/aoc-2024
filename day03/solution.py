def star1(prg: str) -> int:
    """Return sum of all valid multiplications."""
    muls = parse_muls(prg)
    print(len(muls))
    print(muls)
    vals = [exec_mul(m) for m in muls]
    return sum(vals)


def star2():
    input = read_input("input.txt")


def is_valid_number(t: str) -> bool:
    n = int(t) if t.isnumeric() else 0
    return str(n) == t and len(t) >= 1 and len(t) <= 3


def parse_muls(prg: str) -> list[str]:
    """Extract valid mul operations from string."""
    muls = []
    [_garbage, *parts] = prg.split("mul(")
    # parse each block that starts with mul( and check if following values fit
    for p in parts:
        m = "mul("
        [v1, *rest] = p.split(",")
        if is_valid_number(v1):
            m += v1 + ","
            [v2, *rest] = rest[0].split(")")
            if is_valid_number(v2):
                m += v2 + ")"
                muls.append(m)
    return muls


def exec_mul(mul: str) -> int:
    """Execute a single multiplication command."""
    [v1, v2] = mul[4:-1].split(",")
    return int(v1) * int(v2)


def read_input(filepath: str) -> str:
    """Read input and parse it."""
    cmd = ""
    with open(filepath, "r") as f:
        for line in f.readlines():
            cmd += line
    return cmd


if __name__ == "__main__":
    input = read_input("input.txt")
    v = star1(input)
    print(f"⭐️Star 1: {v}")
    # 160683556 too high
    print("🌟Star 2:")
    # star2()
