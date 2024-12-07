# Effort
# Part1: 30 + 10 + 60
# Part2:

from __future__ import annotations
import copy
type Puzzle = list[list[chr]]


class P2D:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return P2D(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return P2D(self.x + other.x, self.y + other.y)


class Letter(P2D):

    def __init__(self, x: int, y: int, character: chr):
        super().__init__(x, y)
        self.character = character


class Word:
    def __init__(self, character: str, x: int, y: int, puzzle: Puzzle):
        self.chars = [character]
        self.puzzle = puzzle
        self.pos = P2D(x, y)
        self.dir = P2D(0, 0)
        self.is_valid = True
        self.children: list[Word] = []

    @property
    def neighbors(self) -> list[Letter]:
        """Get neighboring elements from the puzzle."""
        x = self.pos.x
        y = self.pos.y
        puzzle = self.puzzle
        neighbors: list[Letter] = []
        if x > 1:
            l = Letter(x-1, y, puzzle[y][x-1])
            neighbors.append(l)
            if y > 1:
                l = Letter(x-1, y-1, puzzle[y-1][x-1])
                neighbors.append(l)
            if y < len(puzzle) - 1:
                l = Letter(x-1, y+1, puzzle[y+1][x-1])
                neighbors.append(l)
        if x < len(puzzle[y]) - 1:
            l = Letter(x+1, y, puzzle[y][x+1])
            neighbors.append(l)
            if y > 1:
                l = Letter(x+1, y-1, puzzle[y-1][x+1])
                neighbors.append(l)
            if y < len(puzzle) - 1:
                l = Letter(x+1, y+1, puzzle[y+1][x+1])
                neighbors.append(l)
        if y > 1:
            l = Letter(x, y-1, puzzle[y-1][x])
            neighbors.append(l)
        if y < len(puzzle) - 1:
            l = Letter(x, y+1, puzzle[y+1][x])
            neighbors.append(l)
        return neighbors

    @property
    def is_complete(self):
        return len(self.chars) == 4 and "X" in self.chars and "M" in self.chars and "A" in self.chars and "S" in self.chars

    @property
    def next_letter(self):
        """Next letter to be found. Only works in one direction."""
        match self.chars[-1]:
            case "X":
                return "M"
            case "M":
                return "A"
            case "A":
                return "S"

    def check_next(self) -> list[Word]:
        """Check if next letter of word exists in direction.

        Returns all possible words that exist from there on."""
        neighbors = self.neighbors

        if (self.dir.x == 0 and self.dir.y == 0):
            # check all possible neighbors
            next_letter = self.next_letter
            for n in neighbors:
                if n.character == next_letter:
                    w = Word(next_letter, n.x, n.y, self.puzzle)
                    w.chars = copy.copy(self.chars)
                    w.chars.append(next_letter)
                    w.dir = w - self
                    self.children.append(w)
        else:
            dx = self.dir.x
            dy = self.dir.y
            nx = self.pos.x + dx
            ny = self.pos.y + dy
            puzzle = self.puzzle
            if (nx < 0 or nx >= self.len(puzzle[0])):
                self.is_valid = False
                return []
            if (ny < 0 or ny >= self.len(puzzle)):
                self.is_valid = False
                return []
            if puzzle[ny][nx] == self.next_letter:
                w = Word(self.next_letter, nx, ny, self.puzzle)
                w.chars = self.chars
                w.chars.append(next_letter)
                w.dir = self.dir
                self.children.append(w)
            else:
                self.is_valid = False
                return []
        return self.children

    def __sub__(self, other):
        return self.pos - other.pos


def star1(puzzle: Puzzle) -> int:
    """Count the number of XMAS."""
    words: list[Word] = []
    for y in range(len(puzzle)):
        row = puzzle[y]
        for x in range(len(row)):
            v = puzzle[y][x]
            if v == "X":
                w = Word(v, x, y, puzzle)
                words.append(w)
    possible_words = copy.copy(words)
    complete_words: list[Word] = []
    while len(possible_words):
        # loop until the word is complete or failed
        for ix, w in enumerate(possible_words):
            if w.is_complete:
                possible_words.pop(ix)
                complete_words.append(w)
            else:
                new_words = w.check_next()
                possible_words + new_words
                possible_words.pop(ix)

    return len(complete_words)


def get_neighbors(x: int, y: int, puzzle: Puzzle) -> list[chr]:
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


def eliminate_AM(puzzle_in: Puzzle) -> Puzzle:
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


def star2(p: Puzzle) -> int:
    return 0


def read_input(filepath: str) -> Puzzle:
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
