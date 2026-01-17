def parse(input):
    plan = []
    for row in input.splitlines():
        row = [1 if char == "@" else 0 for char in row]
        row.insert(0, 0)
        row.append(0)
        plan.append(row)
    size = len(plan[0])
    plan.insert(0, [0] * size)
    plan.append([0] * size)
    return plan


def accessible(plan):
    height, width = len(plan), len(plan[0])
    for y in range(height):
        for x in range(width):
            if plan[y][x]:
                adjacent = sum(
                    plan[yi][xi]
                    for yi in range(y - 1, y + 2)
                    for xi in range(x - 1, x + 2)
                )
                if adjacent < 5:  # includes tested roll
                    yield (x, y)


def remove_accessible(plan):
    nfree = 0
    while free := list(accessible(plan)):
        nfree += len(free)
        for x, y in free:
            plan[y][x] = 0
    return nfree


def bells(input):
    plan = parse(input)
    yield plan

    yield sum(1 for _ in accessible(plan))

    yield remove_accessible(plan)


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    import sys

    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    print(f"sack: filename: {input_filename}")
    jingle(input_filename)
