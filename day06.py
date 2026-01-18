def parse(input):
    *num_lines, ops_line = input.splitlines()
    rows = [list(map(int, row.split())) for row in num_lines]
    rows.append(ops_line.split())
    return list(zip(*rows))

def krakow(col):
    import math
    [*nums, op] = col
    return (sum if op == "+" else math.prod)(nums)
    
def bells(input):
    columns = parse(input)
    print(columns, "\n")

    yield columns

    yield sum(krakow(col) for col in columns)

    yield None


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    import sys
    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    print(f"sack: filename: {input_filename}")
    jingle(input_filename)
