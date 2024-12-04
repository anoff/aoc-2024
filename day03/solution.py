import re


def star1(prg: str) -> int:
    """Return sum of all valid multiplications."""
    muls = parse_muls(prg)
    vals = [exec_mul(m) for m in muls]
    return sum(vals)


def star2(prg: str) -> int:
    """Return sum of all valid multiplications.

    Ignoring statements if they have a don't() in front."""
    val = 0
    dos = prg.split("do()")
    for d in dos:
        [p, *dont] = d.split("don't()")
        muls = parse_muls(p)
        val += sum([exec_mul(m) for m in muls])
    return val


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
            [v2, *rest] = ",".join(rest).split(")")
            if is_valid_number(v2):
                m += v2 + ")"
                muls.append(m)
    return muls


def exec_mul(mul: str) -> int:
    """Execute a single multiplication command."""
    [v1, v2] = mul[4:-1].split(",")
    # print(f"{v1}:{v2}")
    return int(v1) * int(v2)


def read_input(filepath: str) -> str:
    """Read input and parse it."""
    cmd = ""
    with open(filepath, "r") as f:
        for line in f.read():
            cmd += line
    return cmd


def star1_regex(prg: str) -> int:
    r = re.compile(r"mul\((\d+),(\d+)\)")
    matches = re.findall(r, prg)
    sum = 0
    for m in matches:
        (v1, v2) = m
        sum += int(v1) * int(v2)
        # print(f"{v1}:{v2}")
    return sum


if __name__ == "__main__":
    input = read_input("input.txt")
    v = star1(input)
    print(f"⭐️Star 1: {v}")
    v = star2(input)
    print(f"⭐️Star 2: {v}")
