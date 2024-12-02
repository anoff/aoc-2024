def star1():
    input = read_input("input.txt")
    (a,b) = input
    a.sort()
    b.sort()
    s = get_diff(a, b)
    print(s)

def star2():
    input = read_input("input.txt")
    (a,b) = input
    s = get_similarity(a, b)
    print(s)

def get_diff(list1: list[int], list2: list[int]) -> int:
    """Calculate the difference between the first elements of each list."""
    sum = 0
    for a,b in zip(list1, list2):
        diff = abs(a-b)
        sum += diff
    return sum

def get_similarity(list1: list[int], list2: list[int]) -> int:
    """Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list."""
    sum = 0
    for a in list1:
        score = a * list2.count(a)
        sum += score
    return sum


def read_input(filepath: str) -> tuple[list[int]]:
    """Read input and parse it."""
    first = []
    second = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            [a,b] = line.split("   ")
            first.append(int(a))
            second.append(int(b))
    return (first, second)

if __name__ == "__main__":
    print("⭐️Star 1:")
    star1()
    print("🌟Star 2:")
    star2()