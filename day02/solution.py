def star1():
    input = read_input("input.txt")
    safe_cnt = 0
    for r in input:
        if is_safe(r):
            safe_cnt += 1
    print(safe_cnt)


def star2():
    input = read_input("input.txt")
    safe_cnt = 0
    for r in input:
        if is_safe_dampened(r):
            safe_cnt += 1
    print(safe_cnt)


def is_safe(report: list[int]) -> bool:
    """Check if a report is safe or not.

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three."""

    is_increasing = (report[1] - report[0]) > 0
    for ix, l in enumerate(report[1:]):
        diff = l - report[ix]
        if (is_increasing and diff < 0) or (not is_increasing and diff > 0):
            return False
        if abs(diff) < 1 or abs(diff) > 3:
            return False
    return True


def is_safe_dampened1(report: list[int]) -> bool:
    """Check if a report is safe or not.

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
    Tolerate a single bad level in what would otherwise be a safe report."""

    is_increasing = (report[1] - report[0]) > 0
    bad_items = 0
    for ix, l in enumerate(report[1:]):
        diff = l - report[ix-bad_items]  # treat as offset to skip bad item
        if (is_increasing and diff < 0) or (not is_increasing and diff > 0):
            if bad_items == 0:
                bad_items += 1
                continue
            return False
        if abs(diff) < 1 or abs(diff) > 3:
            if bad_items == 0:
                bad_items += 1
                continue
            return False
    return True


def is_safe_dampened(report: list[int]) -> bool:
    """Check if a report is safe or not.

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
    Tolerate a single bad level in what would otherwise be a safe report."""

    diff = [report[i + 1] - report[i] for i in range(len(report)-1)]
    no_highchange = sum([1 for v in diff if abs(v) > 3 or abs(v) < 1])
    no_inc = sum([1 for v in diff if v > 0])
    no_dec = sum([1 for v in diff if v < 0])
    return no_highchange < 2 and ((no_inc < 2 and no_dec > 0) or (no_inc > 0 and no_dec < 2))


def read_input(filepath: str) -> list[list[int]]:
    """Read input and parse it."""
    reports = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            numbers = line.split(" ")
            reports.append([int(n) for n in numbers])
    return reports


if __name__ == "__main__":
    print("⭐️Star 1:")
    star1()
    print("🌟Star 2:")
    star2()
# 263 too low
