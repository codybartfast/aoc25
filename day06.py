def parse1(input):
    *num_lines, ops_line = input.splitlines()
    rows = [list(map(int, row.split())) for row in num_lines]
    rows.append(ops_line.split())
    return list(zip(*rows))


def parse2(input):
    cols = list(zip(*input.splitlines()))

    chunks = []
    chunk = []
    for col in cols:
        if all(char == " " for char in col):
            chunks.append(chunk)
            chunk = []
        else:
            chunk.append(list(col))
    chunks.append(chunk)

    exercises = []
    for chunk in chunks:
        nums_op = [int("".join(col[:-1])) for col in chunk]
        op = [char for char in [col[-1] for col in chunk] if char != " "][0]
        nums_op.append(op)
        exercises.append(nums_op)
    return exercises


def apply(nums_op):
    import math

    [*nums, op] = nums_op
    return (sum if op == "+" else math.prod)(nums)


def bells(input):
    exs1 = parse1(input)
    exs2 = parse2(input)

    yield None
    yield sum(apply(nums_op) for nums_op in exs1)
    yield sum(apply(nums_op) for nums_op in exs2)


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    import sys

    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    print(f"sack: filename: {input_filename}")
    jingle(input_filename)
