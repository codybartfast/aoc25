def parse(input):
    [part1, part2] = input.split("\n\n")
    id_ranges = [tuple(map(int, line.split('-'))) for line in part1.splitlines() ]
    ids = list(map(int, part2.splitlines()))
    return id_ranges, ids

def is_in_naive(id, id_ranges):
    for start, end in id_ranges:
        if start <= id and id <= end:
            return True
    return False

def bells(input):
    id_ranges, ids = parse(input)

    yield

    yield len([id for id in ids if is_in_naive(id, id_ranges)])

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
