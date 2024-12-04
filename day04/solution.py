# Effort
# Part1: 30 +
# Part2:
import copy
type puzzle = list[list[chr]]


def star1(p1: puzzle) -> int:
    """Count the number of XMAS."""
    p2 = eliminate_AM(p1)
    for r in p2:
        print("".join(r))

    for r in p1:
        print("".join(r))
    return 0


def get_neighbors(x: int, y: int, puzzle: puzzle) -> list[chr]:
    """Get neighboring elements from the puzzle for given coordinates.

    x = col, y = row"""
    neighbors = []
    if x > 1:
        neighbors.append(puzzle[y][x-1])
        if y > 1:
            neighbors.append(puzzle[y-1][x-1])
        if y < len(puzzle) - 1:
            neighbors.append(puzzle[y+1][x-1])
    if x < len(puzzle[y]) - 1:
        neighbors.append(puzzle[y][x+1])
        if y > 1:
            neighbors.append(puzzle[y-1][x+1])
        if y < len(puzzle) - 1:
            neighbors.append(puzzle[y+1][x+1])
    if y > 1:
        neighbors.append(puzzle[y-1][x])
    if y < len(puzzle) - 1:
        neighbors.append(puzzle[y+1][x])
    return neighbors


def eliminate_AM(puzzle_in: puzzle) -> puzzle:
    """Replace all fields where required letters are nowhere around."""
    puzzle = copy.deepcopy(puzzle_in)
    for y in range(len(puzzle)):
        row = puzzle[y]
        for x in range(len(row)):
            v = puzzle[y][x]
            n = get_neighbors(x, y, puzzle)
            if v == "X":
                if "M" not in n:
                    puzzle[y][x] = "."
            elif v == "M":
                if "X" not in n or "A" not in n:
                    puzzle[y][x] = "."
            elif v == "A":
                if "M" not in n or "S" not in n:
                    puzzle[y][x] = "."
            elif v == "S":
                if "A" not in n:
                    puzzle[y][x] = "."
    return puzzle


def star2(p: puzzle) -> int:
    return 0


def read_input(filepath: str) -> puzzle:
    """Read input and parse it."""
    p = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            p.append(list(line.strip()))
    return p


if __name__ == "__main__":
    input = read_input("input.txt")
    v = star1(input)
    print(f"⭐️Star 1: {v}")
    # v = star2(input)
    # print(f"⭐️Star 2: {v}")
